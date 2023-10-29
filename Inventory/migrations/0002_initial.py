# Generated by Django 4.2.6 on 2023-10-29 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventory', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorybook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.AddField(
            model_name='inventorybook',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.inventory'),
        ),
    ]
