# Generated by Django 2.2.3 on 2019-09-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0030_auto_20190911_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryitems',
            name='nbr_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
