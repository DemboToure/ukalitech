# Generated by Django 2.2.3 on 2019-08-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_auto_20190725_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
    ]
