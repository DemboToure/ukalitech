# Generated by Django 2.2.3 on 2019-11-14 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_auto_20191101_2042'),
        ('invoicing', '0014_remove_invoiceitem_bla'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='account',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.PROTECT, to='accounting.Account'),
            preserve_default=False,
        ),
    ]