# Generated by Django 2.2.3 on 2019-07-22 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_auto_20190722_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='label',
            field=models.CharField(max_length=100),
        ),
    ]
