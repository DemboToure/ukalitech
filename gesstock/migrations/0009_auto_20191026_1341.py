# Generated by Django 2.2.3 on 2019-10-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gesstock', '0008_auto_20191026_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='ref',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='ref',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]