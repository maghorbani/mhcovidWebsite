# Generated by Django 3.0.6 on 2020-05-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
