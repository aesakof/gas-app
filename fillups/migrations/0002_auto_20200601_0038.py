# Generated by Django 3.0.5 on 2020-06-01 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')]),
        ),
    ]