# Generated by Django 5.0 on 2024-03-30 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kinopoiskapp', '0004_rename_title_news_titl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='titl',
            new_name='title',
        ),
    ]
