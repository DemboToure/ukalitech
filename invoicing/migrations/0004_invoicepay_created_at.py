# Generated by Django 2.2.3 on 2019-11-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0003_invoiceitem_tva'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicepay',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
