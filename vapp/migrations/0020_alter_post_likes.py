# Generated by Django 4.2.3 on 2023-09-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0019_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
