# Generated by Django 2.2.3 on 2019-07-25 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_auto_20190723_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structure', models.CharField(max_length=100)),
                ('begin', models.DateField()),
                ('end', models.DateField()),
                ('post', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Employee')),
            ],
        ),
    ]