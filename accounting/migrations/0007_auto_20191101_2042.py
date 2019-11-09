# Generated by Django 2.2.3 on 2019-11-01 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_auto_20191101_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gesstock.Customer'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gesstock.Provider'),
        ),
    ]
