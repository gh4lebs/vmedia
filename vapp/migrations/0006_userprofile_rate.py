# Generated by Django 4.2.3 on 2023-09-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0005_remove_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rate',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
