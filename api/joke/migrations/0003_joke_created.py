# Generated by Django 3.1.5 on 2021-07-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0002_joke_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]