import string
import random

from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from billing.models.payment import Payment


def generate_transaction_id(size=16, chars=string.ascii_uppercase + string.digits):
    """
    """
    return ''.join(random.choice(chars) for _ in range(size))


def latest_payment(owner):
    """
    """
    try:
        return Payment.payments.filter(owner=owner).latest('started_at')
    except ObjectDoesNotExist:
        return None


def list_payments(owner, statuses=None):
    """
    """
    if statuses is None:
        return list(Payment.payments.filter(owner=owner).all())
    return list(Payment.payments.filter(owner=owner, status__in=statuses).all())


def by_transaction_id(transaction_id):
    """
    """
    return Payment.payments.filter(transaction_id=transaction_id).first()


def start_payment(owner, amount, payment_method):
    """
    """
    new_transaction_id = generate_transaction_id()
    while Payment.payments.filter(transaction_id=new_transaction_id).exists():
        new_transaction_id = generate_transaction_id()
    new_payment = Payment.payments.create(
        owner=owner,
        amount=amount,
        method=payment_method,
        transaction_id=new_transaction_id,
        started_at=timezone.now(),
    )
    return new_payment


def update_payment(payment_object, status=None, merchant_reference=None):
    """
    """
    if status is not None:
        payment_object.status = status
    if merchant_reference is not None:
        payment_object.merchant_reference = merchant_reference
    payment_object.save()
    return payment_object


def finish_payment(transaction_id, status, merchant_reference=None):
    """
    """
    payment_object = by_transaction_id(transaction_id=transaction_id)
    if not payment_object:
        return None
    old_status = payment_object.status
    new_status = status
    payment_object.status = status
    payment_object.finished_at = timezone.now()
    if merchant_reference is not None:
        payment_object.merchant_reference = merchant_reference
    payment_object.save()
    if old_status != new_status and new_status == 'processed':
        payment_object.owner.balance += payment_object.amount
        payment_object.owner.save()
    return payment_object
