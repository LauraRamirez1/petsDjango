# Generated by Django 4.2 on 2023-05-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefonoCliente',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='razaMascota',
            field=models.CharField(max_length=50),
        ),
    ]