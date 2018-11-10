# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-11-10 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media_root/blog/')),
                ('image_height', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('category_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogCategory')),
            ],
        ),
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media_root/blog/')),
                ('image_height', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogDetail')),
            ],
        ),
        migrations.CreateModel(
            name='BlogMainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='PostBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_by', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='Main_Category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogMainCategory'),
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.BlogCategory'),
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='default',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_category', to='blog.BlogCategory'),
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='post_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.PostBy'),
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogMainCategory'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='default',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_main_category', to='blog.BlogMainCategory'),
        ),
    ]