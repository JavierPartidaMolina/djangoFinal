# Generated by Django 2.1.5 on 2019-01-28 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GestionRopa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('Precio', models.IntegerField(verbose_name='precio')),
                ('Talla', models.CharField(max_length=10, verbose_name='talla')),
                ('Imagen', models.ImageField(upload_to='imagenes', verbose_name='imagen')),
                ('Tienda', models.CharField(max_length=50, verbose_name='tienda')),
            ],
        ),
        migrations.CreateModel(
            name='Tejido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='ropa',
            name='Tejido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionRopa.Tejido', verbose_name='tejido'),
        ),
        migrations.AddField(
            model_name='ropa',
            name='Tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionRopa.Tipo', verbose_name='tipo'),
        ),
        migrations.AddField(
            model_name='ropa',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
    ]
