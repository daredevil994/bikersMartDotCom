# Generated by Django 3.0.3 on 2020-03-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfileApp', '0006_auto_20200330_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='../media/profile_pics'),
        ),
    ]
