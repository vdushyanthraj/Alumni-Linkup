# Generated by Django 5.0.2 on 2025-03-14 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_verification_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='verification_code',
        ),
    ]
