# Generated by Django 2.2.3 on 2019-09-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepriseinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepriseinfo',
            name='img',
            field=models.ImageField(blank=True, default='entreprise/default.png', upload_to='entreprise/'),
        ),
    ]