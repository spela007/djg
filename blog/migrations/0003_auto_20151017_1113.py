# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slikca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slikca',
            field=models.ImageField(upload_to='blog/%Y/%m/%d', null=True, default=None),
        ),
    ]
