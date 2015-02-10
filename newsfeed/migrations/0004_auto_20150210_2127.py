# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0003_auto_20150209_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='voter',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='upvote',
            name='voter_set',
            field=models.ForeignKey(related_name='voter_set', default='', to='newsfeed.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follower',
            name='followee_id',
            field=models.ForeignKey(related_name='followee_set', to='newsfeed.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='follower',
            name='follower_id',
            field=models.ForeignKey(related_name='follower_set', to='newsfeed.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='image_path',
            field=models.FilePathField(verbose_name=b'/images/posts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='upvote',
            name='original_poster',
            field=models.ForeignKey(related_name='op_set', to='newsfeed.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar_path',
            field=models.FilePathField(verbose_name=b'/images/avatars'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
