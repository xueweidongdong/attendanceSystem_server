# Generated by Django 3.0.2 on 2020-02-29 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20200227_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='sign',
        ),
    ]