# Generated by Django 2.2.4 on 2019-11-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('identifier', models.IntegerField()),
                ('country', models.CharField(choices=[('GT', 'Guatemala'), ('ELS', 'El Salvador')], max_length=5)),
                ('type', models.CharField(choices=[('Lg', 'Trailer'), ('Md', 'Camiones'), ('Sm', 'Automoviles')], max_length=2)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
