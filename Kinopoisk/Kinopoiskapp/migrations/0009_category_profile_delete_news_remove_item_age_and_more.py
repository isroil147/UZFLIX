# Generated by Django 5.0 on 2024-04-18 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kinopoiskapp', '0008_alter_item_video'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ImageField(default='default.jpg', null=True, upload_to='profile_pciture')),
                ('password1', models.CharField(blank=True, max_length=200, null=True)),
                ('password2', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.RemoveField(
            model_name='item',
            name='age',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
