# Generated by Django 4.2.6 on 2023-10-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_display_poin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='poin',
            field=models.IntegerField(default=0),
        ),
    ]
