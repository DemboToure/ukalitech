# Generated by Django 2.2.3 on 2019-11-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0033_auto_20190919_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
