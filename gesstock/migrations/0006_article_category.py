# Generated by Django 2.2.3 on 2019-10-26 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gesstock', '0005_auto_20191026_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True)),
                ('ref', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gesstock.Category')),
            ],
        ),
    ]
