# Generated by Django 3.1.6 on 2021-03-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_restaurant', '0012_message_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user_email',
            field=models.EmailField(max_length=254),
        ),
    ]