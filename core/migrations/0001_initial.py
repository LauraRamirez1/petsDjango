# Generated by Django 4.2 on 2023-05-06 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigoCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=30)),
                ('telefonoCliente', models.IntegerField()),
                ('correoCliente', models.CharField(max_length=50)),
                ('passCliente', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50)),
                ('precioProducto', models.IntegerField()),
                ('descripcionProducto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMascota', models.CharField(max_length=50)),
                ('nombreCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
            ],
        ),
    ]