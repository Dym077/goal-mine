# Generated by Django 4.2.11 on 2024-04-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
