# Generated by Django 2.2.3 on 2019-07-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190720_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='begin',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='end',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(auto_now=True),
        ),
    ]
