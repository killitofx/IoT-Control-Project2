# Generated by Django 2.0.2 on 2018-03-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alive',
            name='send_data',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
