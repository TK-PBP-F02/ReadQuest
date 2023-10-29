
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('published_date', models.TextField()),
                ('thumbnail', models.URLField()),
                ('publisher', models.CharField(max_length=255)),
                ('publication_date', models.CharField(max_length=100)),
                ('page_count', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('lang', models.CharField(max_length=100)),
                ('readed', models.IntegerField(default=0)),
                ('buys', models.IntegerField(default=0)),
                ('quest_amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BookBought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_bought', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_read', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookReviewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reviewed', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]
