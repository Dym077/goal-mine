# Generated by Django 4.2.11 on 2024-04-24 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_goal_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]