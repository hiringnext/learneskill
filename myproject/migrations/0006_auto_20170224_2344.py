# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-24 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_course_detail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_detail',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
