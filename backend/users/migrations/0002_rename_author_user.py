# Generated by Django 3.2.7 on 2021-09-16 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='User',
        ),
    ]
