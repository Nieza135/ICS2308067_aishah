# Generated by Django 5.1 on 2024-08-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stud_status',
            field=models.CharField(default='Active', max_length=10),
        ),
    ]
