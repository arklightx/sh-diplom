# Generated by Django 4.1.5 on 2023-02-22 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0005_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='documents')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='home.home')),
            ],
        ),
        migrations.CreateModel(
            name='Disablings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=60)),
                ('resource', models.CharField(max_length=60)),
                ('reason', models.CharField(max_length=60)),
                ('disable_dt', models.DateTimeField()),
                ('enable_dt', models.DateTimeField()),
                ('fact_dt', models.DateTimeField(blank=True, null=True)),
                ('aparment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disablings', to='home.apartment')),
            ],
        ),
    ]