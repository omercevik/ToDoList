# Generated by Django 3.1.3 on 2020-12-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_todolist', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('itemName', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('status', models.IntegerField(default=0)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
