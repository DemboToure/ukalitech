# Generated by Django 2.2.3 on 2019-08-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0020_salarydesignation'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarydesignation',
            name='code',
            field=models.IntegerField(default=1),
        ),
    ]
