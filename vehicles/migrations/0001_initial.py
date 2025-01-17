# Generated by Django 2.2.4 on 2019-11-26 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fleets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.SmallIntegerField(default=0)),
                ('down', models.SmallIntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('hour', models.TimeField(auto_now=True)),
                ('lat', models.CharField(max_length=25)),
                ('long', models.CharField(max_length=25)),
                ('direction', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField()),
                ('brand', models.CharField(max_length=30)),
                ('model', models.IntegerField()),
                ('type', models.CharField(choices=[('Lg', 'Trailer'), ('Md', 'Camion'), ('Sm', 'Automovil')], max_length=20)),
                ('color', models.CharField(max_length=30)),
                ('registration_number', models.CharField(max_length=8)),
                ('created', models.DateTimeField(auto_now=True)),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='fleets.Fleet')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('hour', models.TimeField(auto_now=True)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('direction', models.CharField(blank=True, max_length=50, null=True)),
                ('velocity', models.FloatField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='vehicles.Vehicle')),
            ],
        ),
    ]
