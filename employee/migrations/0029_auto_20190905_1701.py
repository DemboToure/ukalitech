# Generated by Django 2.2.3 on 2019-09-05 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0028_salary_salaryitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='salary',
            name='salary_period',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]