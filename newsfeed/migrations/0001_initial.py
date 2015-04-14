# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import newsfeed.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followee_id', models.ForeignKey(related_name='followee_set', to=settings.AUTH_USER_MODEL)),
                ('follower_id', models.ForeignKey(related_name='follower_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_title', models.CharField(max_length=100)),
                ('post_text', models.TextField(max_length=5000)),
                ('image_path', models.ImageField(null=True, upload_to=newsfeed.models.generate_filename, blank=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('owner', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=100)),
                ('post_id', models.ForeignKey(to='newsfeed.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_poster', models.ForeignKey(related_name='op_set', to=settings.AUTH_USER_MODEL)),
                ('post_id', models.ForeignKey(to='newsfeed.Post')),
                ('voter_set', models.ForeignKey(related_name='voter_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
