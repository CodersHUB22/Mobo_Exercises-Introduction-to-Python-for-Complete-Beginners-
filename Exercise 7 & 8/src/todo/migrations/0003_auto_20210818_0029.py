# Generated by Django 3.2.6 on 2021-08-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='modified_date',
            field=models.DateTimeField(null=True),
        ),
    ]
