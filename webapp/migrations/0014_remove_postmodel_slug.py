# Generated by Django 4.0 on 2022-02-15 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_alter_postmodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='slug',
        ),
    ]
