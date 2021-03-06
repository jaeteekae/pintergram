# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post_id',
            field=models.ForeignKey(related_name='tags', to='newsfeed.Post'),
            preserve_default=True,
        ),
    ]
