# Generated by Django 4.2.6 on 2023-10-29 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaderboard', '0004_alter_display_poin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='poin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]