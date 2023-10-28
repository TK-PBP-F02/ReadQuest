

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
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('published_date', models.TextField()),
                ('thumbnail', models.URLField()),
                ('readed', models.IntegerField(default=0)),
                ('buys', models.IntegerField(default=0)),
                ('quest_amount', models.IntegerField(default=0)),
            ],
        ),
    ]
