# Generated by Django 2.2.3 on 2019-07-21 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20190721_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='cni_img',
        ),
    ]
