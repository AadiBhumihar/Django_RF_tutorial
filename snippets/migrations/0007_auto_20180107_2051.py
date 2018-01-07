# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0006_auto_20180107_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='person',
        ),
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(related_name='snippets', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
