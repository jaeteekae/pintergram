# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='post_text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_title',
        ),
    ]
