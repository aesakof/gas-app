# Generated by Django 3.0.5 on 2020-06-02 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fillups', '0002_auto_20200601_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fillup',
            name='mpg',
        ),
    ]
