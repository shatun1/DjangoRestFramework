# Generated by Django 3.2.7 on 2021-09-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0003_alter_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link_to_repo',
            field=models.URLField(blank=True, max_length=1024),
        ),
    ]
