# Generated by Django 2.2.4 on 2022-10-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_AuthersApp', '0002_authers_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authers',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
