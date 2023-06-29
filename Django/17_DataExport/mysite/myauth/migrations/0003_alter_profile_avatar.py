# Generated by Django 4.1.6 on 2023-04-03 09:28

from django.db import migrations, models
import myauth.models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=myauth.models.avatar_preview_directory_path),
        ),
    ]
