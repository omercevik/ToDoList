# Generated by Django 3.1.3 on 2020-12-02 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new_todolist', '0006_auto_20201201_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]