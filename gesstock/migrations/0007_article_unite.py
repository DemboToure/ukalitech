# Generated by Django 2.2.3 on 2019-10-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gesstock', '0006_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='unite',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
