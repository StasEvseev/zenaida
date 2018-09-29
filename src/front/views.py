from django.shortcuts import render, redirect

from back.domains import list_domains
from front.forms import DomainLookupForm
from zepp.zmaster import domain_check


def domain_lookup(request):
    if not request.user.is_authenticated:
        return redirect('index')
    result = ''
    if request.method != 'POST':
        form = DomainLookupForm()
    else:
        form = DomainLookupForm(request.POST)
        if form.is_valid():
            result = domain_check(domain=form.cleaned_data['domain_name'], return_string=True)
    return render(request, 'front/domain_lookup.html', {'form': form, 'result': result, }, )


def account_overview(request):
    if not request.user.is_authenticated:
        return redirect('index')
    result = ''
    return render(request, 'front/account_overview.html', {'result': result, }, )


def account_domains(request):
    if not request.user.is_authenticated:
        return redirect('index')
    domains_list = list_domains(request.user.email)
    return render(request, 'front/account_domains.html', {
        'domains': domains_list,
    }, )
