# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_auto_20150207_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followee_id', models.ForeignKey(related_name='+', to='newsfeed.User')),
                ('follower_id', models.ForeignKey(related_name='+', to='newsfeed.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_poster', models.ForeignKey(related_name='+', to='newsfeed.User')),
                ('post_id', models.ForeignKey(to='newsfeed.Post')),
                ('voter', models.ForeignKey(related_name='+', to='newsfeed.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'0000', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
