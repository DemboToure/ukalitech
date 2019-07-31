# Generated by Django 2.2.3 on 2019-07-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntrepriseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('entreprise_type', models.CharField(blank=True, choices=[('personnal', 'personnel'), ('GIE', 'GIE'), ('SA', 'SA'), ('SARL', 'SARL')], max_length=20)),
                ('adress', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('contact_2', models.CharField(blank=True, max_length=50)),
                ('ninea_number', models.CharField(max_length=50)),
            ],
        ),
    ]
