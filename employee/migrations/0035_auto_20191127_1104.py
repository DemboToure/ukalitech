# Generated by Django 2.2.3 on 2019-11-27 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0034_auto_20191127_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='end',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
