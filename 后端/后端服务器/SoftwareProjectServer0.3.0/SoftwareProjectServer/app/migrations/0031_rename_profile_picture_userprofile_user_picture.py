# Generated by Django 4.2.6 on 2023-12-28 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_userprofile_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_picture',
            new_name='user_picture',
        ),
    ]
