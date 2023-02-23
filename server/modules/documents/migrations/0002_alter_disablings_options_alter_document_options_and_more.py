# Generated by Django 4.1.5 on 2023-02-23 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_apartment_options_alter_home_options_and_more'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disablings',
            options={'verbose_name': 'Отключение', 'verbose_name_plural': 'Отключения'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterField(
            model_name='disablings',
            name='aparment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disablings', to='home.apartment', verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='disablings',
            name='disable_dt',
            field=models.DateTimeField(verbose_name='Дата отключения'),
        ),
        migrations.AlterField(
            model_name='disablings',
            name='enable_dt',
            field=models.DateTimeField(verbose_name='Дата включения'),
        ),
        migrations.AlterField(
            model_name='disablings',
            name='fact_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Фактическая дата включения'),
        ),
        migrations.AlterField(
            model_name='disablings',
            name='reason',
            field=models.CharField(max_length=60, verbose_name='Причина отключения'),
        ),
        migrations.AlterField(
            model_name='disablings',
            name='resource',
            field=models.CharField(max_length=60, verbose_name='Отключаемый ресурс'),
        ),
        migrations.AlterField(
            model_name='disablings',
            name='status',
            field=models.CharField(max_length=60, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='document',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='home.home', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Тайтл'),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(max_length=120, verbose_name='Тип документа'),
        ),
    ]