# Generated by Django 5.1.2 on 2024-10-28 08:05

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_quality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=221, null=True, verbose_name='Nomi')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 28, 13, 5, 1, 706593), null=True, verbose_name="Qo'shilgan vaqti")),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Kompaniyalar',
                'db_table': 'company',
            },
        ),
        migrations.AlterField(
            model_name='users',
            name='joined_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 28, 13, 5, 1, 706593), null=True, verbose_name="Qo'shilgan vaqti"),
        ),
        migrations.CreateModel(
            name='Qualities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_quantity', models.IntegerField(blank=True, null=True, verbose_name='Zakaz qilingan mahsulotlar soni')),
                ('delivered_quantity', models.IntegerField(blank=True, null=True, verbose_name='Keltirilgan mahsulotlar soni')),
                ('percent_products', models.FloatField(blank=True, null=True, verbose_name='Kelishilgan mahsulotlarning yetkazib berilganlik foizi')),
                ('invalid_quantity', models.IntegerField(blank=True, null=True, verbose_name='Yaroqsiz mahsulotlar soni')),
                ('agreed_time', models.DateTimeField(blank=True, null=True, verbose_name='Yetkazib berish kelishilgan vaqt')),
                ('delivered_time', models.DateTimeField(blank=True, null=True, verbose_name='Yetkazib berilgan vaqt')),
                ('percent_time', models.FloatField(blank=True, null=True, verbose_name='Kelishilgan vaqtda yetkazib berilish foizi')),
                ('percentage_quality', models.FloatField(blank=True, null=True, verbose_name='Mahsulotlar sifati foizi')),
                ('average_percentage', models.FloatField(blank=True, null=True, verbose_name='Umumiy sifat foizi')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 28, 13, 5, 1, 706593), null=True, verbose_name='Yaratilgan vaqti')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='check_quality.companies', verbose_name='Kompaniya')),
            ],
            options={
                'verbose_name': 'Quality',
                'verbose_name_plural': 'Yetkazilgan mahsulotlar sifati',
                'db_table': 'quality',
            },
        ),
    ]
