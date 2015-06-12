# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(default=b'Original', max_length=50)),
                ('nit', models.PositiveIntegerField()),
                ('fecha_fun', models.DateField()),
                ('direccion', models.CharField(max_length=50, blank=True)),
                ('tipo', models.CharField(default=b'Otros', max_length=20, choices=[(b'Comercial', b'Comercial'), (b'Industrial', b'Industrial'), (b'Servicio', b'Servicio'), (b'Otros', b'Otros')])),
                ('obj_actividad', models.CharField(max_length=50, blank=True)),
                ('acronimo', models.CharField(max_length=15, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('fax', models.CharField(max_length=50, blank=True)),
                ('telefono', models.PositiveIntegerField(null=True, blank=True)),
                ('logo', models.ImageField(upload_to=b'/logo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
