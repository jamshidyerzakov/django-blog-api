# Generated by Django 3.0.6 on 2020-06-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200612_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_posts',
        ),
    ]
