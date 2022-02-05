# Generated by Django 4.0.1 on 2022-02-05 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('dashboard', '0002_remove_features_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='features',
            old_name='Acceleration',
            new_name='acceleration',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Aggression',
            new_name='aggression',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Agility',
            new_name='agility',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Balance',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='BallControl',
            new_name='ballControl',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Composure',
            new_name='composure',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Curve',
            new_name='curve',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Dribbling',
            new_name='dribbling',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='FKAccuracy',
            new_name='fKAccuracy',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Finishing',
            new_name='finishing',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='GKDiving',
            new_name='gKDiving',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='GKHandling',
            new_name='gKHandling',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='GKKicking',
            new_name='gKKicking',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='GKPositioning',
            new_name='gKPositioning',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='GKReflexes',
            new_name='gKReflexes',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='HeadingAccuracy',
            new_name='headingAccuracy',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Interceptions',
            new_name='interceptions',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Jumping',
            new_name='jumping',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='LongPassing',
            new_name='longPassing',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='LongShots',
            new_name='longShots',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Marking',
            new_name='marking',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Penalties',
            new_name='penalties',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Positioning',
            new_name='positioning',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Reactions',
            new_name='reactions',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='ShortPassing',
            new_name='shortPassing',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='ShotPower',
            new_name='shotPower',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='SlidingTackle',
            new_name='slidingTackle',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='SprintSpeed',
            new_name='sprintSpeed',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Stamina',
            new_name='stamina',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='StandingTackle',
            new_name='standingTackle',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Strength',
            new_name='strength',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Vision',
            new_name='vision',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='Volleys',
            new_name='volleys',
        ),
        migrations.AddField(
            model_name='features',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
            preserve_default=False,
        ),
    ]
