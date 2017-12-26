# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=200)),
                ('contenuto', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
