# Generated by Django 3.2.8 on 2021-10-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewsit_app', '0002_channelposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelposts',
            name='slug_url',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='channelposts',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
