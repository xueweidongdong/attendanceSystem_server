# Generated by Django 3.0.2 on 2020-02-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_remove_attendance_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='number',
            field=models.CharField(default='40', max_length=200),
        ),
    ]
