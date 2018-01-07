# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0003_auto_20180106_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
        migrations.AddField(
            model_name='snippet',
            name='person',
            field=models.ForeignKey(related_name='snippets', blank=True, to='snippets.Person', null=True),
        ),
    ]
