# Generated by Django 3.0.6 on 2020-05-23 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
