# Generated by Django 3.1.3 on 2020-12-04 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_todolist', '0008_todolists'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='userId',
            new_name='listId',
        ),
    ]
