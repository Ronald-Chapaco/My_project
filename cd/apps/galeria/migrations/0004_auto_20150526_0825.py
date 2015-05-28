# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_auto_20150519_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='user',
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='user',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Fotos',
        ),
    ]
