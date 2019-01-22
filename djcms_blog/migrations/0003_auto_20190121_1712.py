# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djcms_blog', '0002_auto_20190120_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttitle',
            old_name='publisher_is_draft',
            new_name='is_draft',
        ),
        migrations.AddField(
            model_name='posttitle',
            name='public_post_title',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='post_draft', to='djcms_blog.PostTitle'),
        ),
        migrations.RemoveField(
            model_name='posttitle',
            name='publisher_public',
        ),
        migrations.AlterUniqueTogether(
            name='posttitle',
            unique_together=set([('post', 'language', 'is_draft')]),
        ),
    ]
