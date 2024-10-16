# Generated by Django 5.1 on 2024-09-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentor',
            fields=[
                ('mentor_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('mentor_name', models.CharField(max_length=200)),
                ('mentor_room_no', models.CharField(default='sk2', max_length=10)),
            ],
        ),
    ]
