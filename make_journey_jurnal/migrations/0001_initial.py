# Generated by Django 4.2.6 on 2023-10-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField()),
                ('author', models.CharField(default='', max_length=255)),
                ('publisher', models.CharField(default='', max_length=255)),
                ('publication_date', models.CharField(default='', max_length=100)),
                ('page_count', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=255)),
                ('image_url', models.URLField()),
                ('lang', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
