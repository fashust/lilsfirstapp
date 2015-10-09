# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texts_field', models.CharField(max_length=200)),
                ('decimal_field', models.DecimalField(max_digits=12, decimal_places=3)),
            ],
        ),
    ]
