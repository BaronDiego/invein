# Generated by Django 4.1.7 on 2023-02-22 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('programado', models.FloatField(blank=True, max_length=5, null=True)),
                ('avance', models.FloatField(blank=True, max_length=5, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True, verbose_name='Usuario que modifica')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario que Crea')),
            ],
            options={
                'ordering': ['creado'],
            },
        ),
    ]
