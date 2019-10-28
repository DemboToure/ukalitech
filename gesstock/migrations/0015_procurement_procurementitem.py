# Generated by Django 2.2.3 on 2019-10-26 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gesstock', '0014_auto_20191026_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procurementDate', models.DateField()),
                ('received', models.BooleanField(default=False)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gesstock.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gesstock.Article')),
                ('procurement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gesstock.Procurement')),
            ],
        ),
    ]
