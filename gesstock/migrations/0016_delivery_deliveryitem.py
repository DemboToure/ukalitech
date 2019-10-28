# Generated by Django 2.2.3 on 2019-10-28 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gesstock', '0015_procurement_procurementitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryDate', models.DateField()),
                ('delivered', models.BooleanField(default=False)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gesstock.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gesstock.Article')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gesstock.Delivery')),
            ],
        ),
    ]
