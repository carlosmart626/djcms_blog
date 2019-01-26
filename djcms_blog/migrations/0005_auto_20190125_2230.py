# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-25 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djcms_blog', '0004_auto_20190125_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttitle',
            name='public_post_title',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_draft', to='djcms_blog.PostTitle'),
        ),
    ]