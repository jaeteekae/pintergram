# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newsfeed.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0006_auto_20150211_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_path',
            field=models.ImageField(null=True, upload_to=newsfeed.models.generate_filename, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar_path',
            field=models.FilePathField(verbose_name=b'/images/avatars', blank=True),
            preserve_default=True,
        ),
    ]
