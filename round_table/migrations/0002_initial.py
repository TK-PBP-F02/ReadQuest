
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('round_table', '0001_initial'),
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='replies',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='replies',
            name='parent_forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='round_table.forum'),
        ),
        migrations.AddField(
            model_name='forum',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forum',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
