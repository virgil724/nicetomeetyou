# Generated by Django 5.0.6 on 2024-07-07 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('content', models.TextField()),
                ('update_time', models.DateTimeField()),
                ('paper', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='News_Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgUrl', models.URLField()),
                ('comment', models.CharField(max_length=20)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba_news.news')),
            ],
        ),
    ]
