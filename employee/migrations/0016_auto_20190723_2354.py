# Generated by Django 2.2.3 on 2019-07-23 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20190722_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_doc',
            field=models.FileField(null=True, upload_to='employee/'),
        ),
    ]
