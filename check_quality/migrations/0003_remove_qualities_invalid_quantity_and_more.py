# Generated by Django 5.1.2 on 2024-10-28 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_quality', '0002_companies_alter_users_joined_at_qualities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualities',
            name='invalid_quantity',
        ),
        migrations.RemoveField(
            model_name='qualities',
            name='percent_time',
        ),
        migrations.RemoveField(
            model_name='qualities',
            name='percentage_quality',
        ),
        migrations.AddField(
            model_name='qualities',
            name='description_time',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Keltirilgan vaqt haqida izoh'),
        ),
        migrations.AddField(
            model_name='qualities',
            name='quality_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Mahsulotlar sifati haqida izoh'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 28, 17, 51, 58, 787900), null=True, verbose_name="Qo'shilgan vaqti"),
        ),
        migrations.AlterField(
            model_name='qualities',
            name='agreed_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Kelishilgan vaqt'),
        ),
        migrations.AlterField(
            model_name='qualities',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 28, 17, 51, 58, 787900), null=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='qualities',
            name='delivered_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Keltirilgan assortimentlar soni'),
        ),
        migrations.AlterField(
            model_name='qualities',
            name='ordered_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Zakaz qilingan assortimentlar soni'),
        ),
        migrations.AlterField(
            model_name='users',
            name='joined_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 28, 17, 51, 58, 787900), null=True, verbose_name="Qo'shilgan vaqti"),
        ),
    ]
