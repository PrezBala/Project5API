# Generated by Django 3.2.13 on 2023-06-14 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_movie_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created_by',
        ),
    ]