# Generated by Django 3.1.6 on 2021-03-04 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_restaurant', '0008_auto_20210304_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user_email',
        ),
    ]
