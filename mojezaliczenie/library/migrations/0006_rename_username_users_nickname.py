# Generated by Django 4.2.16 on 2025-02-11 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_order_order_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='nickname',
        ),
    ]
