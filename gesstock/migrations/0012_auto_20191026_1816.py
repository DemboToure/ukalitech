# Generated by Django 2.2.3 on 2019-10-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gesstock', '0011_auto_20191026_1651'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Procurement',
            new_name='ProcurementItem',
        ),
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(blank=True, default='gesstock/customer-icon.png', upload_to='gesstock/'),
        ),
    ]