# Generated by Django 2.0.2 on 2018-03-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180321_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='is_change',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
