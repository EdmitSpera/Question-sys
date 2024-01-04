# Generated by Django 4.2.6 on 2023-12-27 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_errors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_email',
            field=models.EmailField(blank=True, error_messages={'unique': '邮箱已存在。'}, max_length=254, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='邮箱格式不正确', regex='^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\\.[a-zA-Z0-9_-]+)+$')], verbose_name='邮箱'),
        ),
    ]
