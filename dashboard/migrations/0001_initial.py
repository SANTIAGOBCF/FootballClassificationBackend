# Generated by Django 4.0.1 on 2022-01-14 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Finishing', models.FloatField()),
                ('HeadingAccuracy', models.FloatField()),
                ('ShortPassing', models.FloatField()),
                ('Volleys', models.FloatField()),
                ('Dribbling', models.FloatField()),
                ('Curve', models.FloatField()),
                ('FKAccuracy', models.FloatField()),
                ('LongPassing', models.FloatField()),
                ('BallControl', models.FloatField()),
                ('Acceleration', models.FloatField()),
                ('SprintSpeed', models.FloatField()),
                ('Agility', models.FloatField()),
                ('Reactions', models.FloatField()),
                ('Balance', models.FloatField()),
                ('ShotPower', models.FloatField()),
                ('Jumping', models.FloatField()),
                ('Stamina', models.FloatField()),
                ('Strength', models.FloatField()),
                ('LongShots', models.FloatField()),
                ('Aggression', models.FloatField()),
                ('Interceptions', models.FloatField()),
                ('Positioning', models.FloatField()),
                ('Vision', models.FloatField()),
                ('Penalties', models.FloatField()),
                ('Composure', models.FloatField()),
                ('Marking', models.FloatField()),
                ('StandingTackle', models.FloatField()),
                ('SlidingTackle', models.FloatField()),
                ('GKDiving', models.FloatField()),
                ('GKHandling', models.FloatField()),
                ('GKKicking', models.FloatField()),
                ('GKPositioning', models.FloatField()),
                ('GKReflexes', models.FloatField()),
                ('position', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
