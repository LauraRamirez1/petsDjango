# Generated by Django 4.2 on 2023-05-08 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cliente_telefonocliente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='correoCliente',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombreCliente',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='passCliente',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='telefonoCliente',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='mascota',
            old_name='nombreCliente',
            new_name='nombre',
        ),
    ]