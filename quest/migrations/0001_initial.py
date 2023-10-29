
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('desc', models.TextField()),
                ('goal', models.CharField(max_length=100)),
                ('point', models.IntegerField(default=10)),
                ('type', models.CharField(default='WordlQuest', max_length=100)),
                ('amount', models.IntegerField(default=1)),
                ('book_id', models.IntegerField(default=0)),
                ('container', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest.questcontainer')),
            ],
        ),
    ]
