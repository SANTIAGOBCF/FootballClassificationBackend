# Generated by Django 4.0.1 on 2022-02-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_features_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
