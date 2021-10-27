# Generated by Django 3.2.8 on 2021-10-27 17:20

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewsit_app', '0004_auto_20211027_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='topic_url',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='channelposts',
            name='channel_post',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='channelposts',
            name='post_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='channelposts',
            name='post_url',
            field=models.URLField(blank=True, default='', max_length=250),
            preserve_default=False,
        ),
    ]
