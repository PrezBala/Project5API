# Generated by Django 3.2.13 on 2023-06-15 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0014_remove_movie_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='auth.user'),
            preserve_default=False,
        ),
    ]
