# Generated by Django 4.2.4 on 2023-10-27 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round_table', '0002_alter_replies_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replies',
            name='parent_replies',
        ),
    ]
