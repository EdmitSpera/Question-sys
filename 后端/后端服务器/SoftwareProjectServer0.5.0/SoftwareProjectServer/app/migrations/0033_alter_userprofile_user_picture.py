# Generated by Django 4.2.6 on 2023-12-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_userprofile_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_picture',
            field=models.BinaryField(blank=True, null=True, verbose_name='头像'),
        ),
    ]
