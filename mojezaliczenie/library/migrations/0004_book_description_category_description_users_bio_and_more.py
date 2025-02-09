# Generated by Django 4.2.16 on 2025-02-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_order_id_order_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='users',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=16, unique=True),
        ),
    ]
