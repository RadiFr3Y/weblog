# Generated by Django 3.2.4 on 2022-01-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_postmodel_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
                ('duration', models.IntegerField(max_length=200)),
                ('cost', models.IntegerField(max_length=200)),
                ('github', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='work_img')),
            ],
        ),
    ]
