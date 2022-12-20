# Generated by Django 4.1.3 on 2022-12-20 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='veterinarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('apellido', models.CharField(max_length=75)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=75)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=75)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.veterinarios')),
            ],
        ),
    ]
