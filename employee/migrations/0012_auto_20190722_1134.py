# Generated by Django 2.2.3 on 2019-07-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_auto_20190722_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='adress',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]