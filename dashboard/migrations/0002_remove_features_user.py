# Generated by Django 4.0.1 on 2022-01-14 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='user',
        ),
    ]
