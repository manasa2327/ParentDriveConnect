# Generated by Django 4.1.7 on 2024-04-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_speeddriver_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentdashboard',
            name='Duration',
            field=models.IntegerField(null=True),
        ),
    ]