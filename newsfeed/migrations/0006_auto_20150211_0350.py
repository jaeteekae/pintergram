# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0005_auto_20150211_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_poster', models.ForeignKey(related_name='op_set', to='newsfeed.User')),
                ('post_id', models.ForeignKey(to='newsfeed.Post')),
                ('voter_set', models.ForeignKey(related_name='voter_set', to='newsfeed.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
