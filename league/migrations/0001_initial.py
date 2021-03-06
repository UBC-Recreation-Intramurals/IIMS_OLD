# Generated by Django 3.2.6 on 2021-08-23 20:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the activity, use a descriptive name users can understand!', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use an easy to read name of the location.', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The pool name, use something descriptive.', max_length=255)),
                ('game_duration', models.DurationField(default=datetime.timedelta(seconds=3600), help_text='The time duration of each game played in this pool.')),
                ('days_of_play', multiselectfield.db.fields.MultiSelectField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], help_text='What days is this pool playing?', max_length=56)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.activity')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.gender')),
                ('locations_of_play', models.ManyToManyField(to='league.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='The first day of the week.')),
                ('end_date', models.DateField(help_text='The last day of the week.')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.pool')),
            ],
        ),
        migrations.AddField(
            model_name='pool',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.term'),
        ),
        migrations.AddField(
            model_name='pool',
            name='tier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.tier'),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start_time', models.TimeField(help_text='Time when the first game can start!')),
                ('end_time', models.TimeField(help_text='Last hour a game can be played this day. (Not the last start time)')),
                ('location', models.ForeignKey(help_text="Location where this day's games are to be played.", on_delete=django.db.models.deletion.CASCADE, to='league.location')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.week')),
            ],
        ),
    ]
