# Generated by Django 4.1.7 on 2023-12-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.JSONField(),
        ),
    ]
