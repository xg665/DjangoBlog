# Generated by Django 3.1.4 on 2021-01-27 05:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20210126_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='problem_num',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(1)]),
        ),
    ]
