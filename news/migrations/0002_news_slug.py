# Generated by Django 2.0.1 on 2018-01-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.CharField(blank=True, max_length=120, unique=True),
        ),
    ]
