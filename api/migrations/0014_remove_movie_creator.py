# Generated by Django 3.2.13 on 2023-06-15 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20230615_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='creator',
        ),
    ]