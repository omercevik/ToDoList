# Generated by Django 3.1.3 on 2020-12-05 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new_todolist', '0009_auto_20201204_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
