# Generated by Django 2.2.4 on 2019-08-31 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('first_name', models.CharField(max_length=140, verbose_name='Nombre Paciente')),
                ('last_name', models.CharField(max_length=140, verbose_name='Apellido Paciente')),
                ('username', models.SlugField(max_length=15, unique=True, verbose_name='Nombre de Usuario Paciente')),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=2, verbose_name='Genero')),
                ('birthdate', models.DateField(verbose_name='Fecha Nacimiento')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
