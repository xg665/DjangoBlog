# Generated by Django 3.1.4 on 2021-01-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
