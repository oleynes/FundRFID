# Generated by Django 3.0.5 on 2020-04-25 00:33

from django.db import migrations, models
import manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('tag_UID', models.CharField(blank=True, max_length=16, verbose_name='Tag UID')),
                ('email', models.EmailField(max_length=254)),
                ('score', models.IntegerField(blank=True)),
                ('img', models.ImageField(blank=True, upload_to=manager.models.create_upload_url, verbose_name='Member Image')),
                ('PAWS_ID', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='PAWS ID')),
                ('class_year', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('SS', 'Super Senior'), ('GR', 'Graduate'), ('AL', 'Alumni')], default='FR', max_length=2)),
            ],
        ),
    ]
