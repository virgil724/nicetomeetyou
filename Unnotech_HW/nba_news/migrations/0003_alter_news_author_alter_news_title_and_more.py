# Generated by Django 5.0.6 on 2024-07-08 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_news', '0002_alter_news_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='news_photo',
            name='comment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news_photo',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_photo', to='nba_news.news'),
        ),
    ]
