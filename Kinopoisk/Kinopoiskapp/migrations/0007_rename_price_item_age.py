# Generated by Django 5.0 on 2024-04-11 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kinopoiskapp', '0006_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='age',
        ),
    ]