# Generated by Django 4.2 on 2023-05-08 15:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('torrent', models.FileField(upload_to='torrents/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['torrent'])])),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dialy_application.category')),
            ],
            options={
                'ordering': ['time_create', 'title'],
            },
        ),
    ]