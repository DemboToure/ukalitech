# Generated by Django 2.2.3 on 2019-11-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0002_auto_20191104_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='tva',
            field=models.IntegerField(default=18),
        ),
    ]
