# Generated by Django 4.1.5 on 2023-02-23 23:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_home_jitsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='jitsi',
            field=models.CharField(default=uuid.UUID('e6c4b121-10f4-4cf1-b703-08a3fe9d06f8'), max_length=128, unique=True),
        ),
    ]
