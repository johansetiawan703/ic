# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-23 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_followers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
