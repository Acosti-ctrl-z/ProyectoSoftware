# Generated by Django 4.2.21 on 2025-05-26 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratorios', '0001_initial'),
        ('Medicamentos', '0002_remove_medicamento_laboratorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='laboratorio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Laboratorios.laboratorios'),
        ),
    ]
