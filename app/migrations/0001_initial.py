# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(choices=[('ALE', 'Alemanha'), ('ARG', 'Argentina'), ('BRA', 'Brasil'), ('CAN', 'Canadá'), ('ESP', 'Espanha'), ('EUA', 'Estados Unidos'), ('FRA', 'França'), ('ING', 'Inglaterra'), ('ITA', 'Itália'), ('NOR', 'Noruega')], max_length=3)),
                ('genero', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.DurationField()),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Artista'),
        ),
        migrations.AddField(
            model_name='album',
            name='musicas',
            field=models.ManyToManyField(to='app.Musica'),
        ),
    ]