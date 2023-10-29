# Generated by Django 4.2.6 on 2023-10-29 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaderboard', '0007_display_form_submit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='display',
            name='form_submit',
        ),
        migrations.RemoveField(
            model_name='display',
            name='poin',
        ),
        migrations.AddField(
            model_name='display',
            name='akun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]