# Generated by Django 3.0.5 on 2020-05-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0005_auto_20200501_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
