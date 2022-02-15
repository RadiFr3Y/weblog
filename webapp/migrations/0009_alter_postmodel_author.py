# Generated by Django 4.0 on 2022-01-20 12:11

import account.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('webapp', '0008_alter_postmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(default=account.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='account.user'),
        ),
    ]