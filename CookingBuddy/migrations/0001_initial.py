# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('session_id', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.CharField(default=b'', max_length=100)),
                ('confidence', models.FloatField(default=0.0)),
                ('utterance', models.CharField(max_length=400)),
                ('current_step', models.IntegerField()),
                ('action', models.CharField(default=b'nothing', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
