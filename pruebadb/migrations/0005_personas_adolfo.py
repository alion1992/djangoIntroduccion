# Generated by Django 3.2.25 on 2024-12-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebadb', '0004_rename_idciudadorigen_usuariosvuelos_idpasajero'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='adolfo',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
