# Generated by Django 5.0 on 2024-03-30 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kinopoiskapp', '0003_result_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='titl',
        ),
    ]
