# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bolt_usersite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Tag Title')),
                ('slug', models.SlugField(max_length=100, verbose_name='Tag Slug')),
                ('posted', models.DateTimeField(auto_now_add=True, verbose_name='Date Posted')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Modified Date')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last Modified Date'),
        ),
        migrations.AddField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last Modified Date'),
        ),
        migrations.AddField(
            model_name='category',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 25, 16, 6, 35, 982679, tzinfo=utc), verbose_name='Date Posted'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name='Blog content'),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='bolt_usersite.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Posted'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Blog slug'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Blog Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Category Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Category Title'),
        ),
    ]
