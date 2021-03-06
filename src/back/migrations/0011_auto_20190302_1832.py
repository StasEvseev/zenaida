# Generated by Django 2.1.7 on 2019-03-02 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0010_auto_20190224_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='contact_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='admin_domains', to='back.Contact', verbose_name='Administrative'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_billing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='billing_domains', to='back.Contact', verbose_name='Billing'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='contact_tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tech_domains', to='back.Contact', verbose_name='Technical'),
        ),
    ]
