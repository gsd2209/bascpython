# Generated by Django 5.1.1 on 2024-10-11 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
