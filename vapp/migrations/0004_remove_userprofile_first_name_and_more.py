# Generated by Django 4.2.3 on 2023-09-15 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0003_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
