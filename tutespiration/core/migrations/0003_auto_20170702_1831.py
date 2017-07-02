# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170702_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='alt_text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
