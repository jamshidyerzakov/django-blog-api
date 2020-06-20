# Generated by Django 3.0.7 on 2020-06-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        ('accounts', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liked_posts',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to='post.Post', verbose_name='Liked Post'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
