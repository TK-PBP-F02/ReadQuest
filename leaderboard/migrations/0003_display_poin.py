# Generated by Django 4.2.6 on 2023-10-28 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaderboard', '0002_display_delete_lboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='display',
            name='poin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]