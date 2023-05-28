# Generated by Django 4.2 on 2023-05-28 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='users',
            field=models.ManyToManyField(related_name='homes', to=settings.AUTH_USER_MODEL, verbose_name='Жильцы'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='home.homelevel', verbose_name='Этаж'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Жилец'),
        ),
    ]