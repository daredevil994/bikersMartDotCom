# Generated by Django 3.0.3 on 2020-03-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfileApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]