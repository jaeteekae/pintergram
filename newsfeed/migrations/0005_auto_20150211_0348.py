# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_auto_20150210_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvote',
            name='original_poster',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='voter_set',
        ),
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]
