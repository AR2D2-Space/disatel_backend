# Generated by Django 2.2.4 on 2019-11-26 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20191125_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'Ya existe un correo con los datos ingresados.'}, max_length=254, verbose_name='Correo'),
        ),
    ]
