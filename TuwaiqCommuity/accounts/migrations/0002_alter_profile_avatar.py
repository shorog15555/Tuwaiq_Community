# Generated by Django 4.2.1 on 2023-06-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/default_avatar.png', upload_to='images/'),
        ),
    ]
