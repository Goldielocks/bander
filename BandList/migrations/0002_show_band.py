# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BandList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='band',
            field=models.ManyToManyField(to='BandList.Band'),
            preserve_default=True,
        ),
    ]
