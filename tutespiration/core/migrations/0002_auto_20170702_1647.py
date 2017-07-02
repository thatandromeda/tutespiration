# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('font_index', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Inspiration',
                'verbose_name_plural': 'Inspirations',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alt_text', models.TextField()),
                ('image_url', models.URLField()),
                ('credit_userid', models.CharField(max_length=30)),
                ('credit_name', models.CharField(max_length=100)),
                ('photo_id', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.AddField(
            model_name='inspiration',
            name='photo',
            field=models.ForeignKey(to='core.Photo'),
        ),
        migrations.AddField(
            model_name='inspiration',
            name='quote',
            field=models.ForeignKey(to='core.Quote'),
        ),
    ]
