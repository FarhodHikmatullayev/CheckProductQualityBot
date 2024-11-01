import datetime
from django.db import models

from app import on_startup


class Users(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'Oddiy foydalanuvchi'),
    )
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='F.I.Sh')
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name='Username')
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True, verbose_name="Telegram ID")
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='user', null=True, blank=True,
                            verbose_name='Foydalanuvchi roli')
    joined_at = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now(),
                                     verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'
        db_table = 'users'

    def __str__(self):
        return self.full_name


class Companies(models.Model):
    name = models.CharField(null=True, blank=True, max_length=221, verbose_name="Nomi")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Kompaniyalar'
        db_table = 'company'

    def __str__(self):
        return self.name


class Qualities(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Kompaniya")
    ordered_quantity = models.IntegerField(null=True, blank=True, verbose_name="Zakaz qilingan assortimentlar soni")
    delivered_quantity = models.IntegerField(null=True, blank=True, verbose_name="Keltirilgan assortimentlar soni")
    percent_products = models.FloatField(null=True, blank=True,
                                         verbose_name="Kelishilgan mahsulotlarning yetkazib berilganlik foizi")
    quality_description = models.CharField(max_length=500, null=True, blank=True,
                                           verbose_name="Mahsulotlar sifati haqida izoh")
    agreed_time = models.DateTimeField(null=True, blank=True, verbose_name="Kelishilgan vaqt")
    delivered_time = models.DateTimeField(null=True, blank=True, verbose_name="Yetkazib berilgan vaqt")
    description_time = models.CharField(max_length=500, null=True, blank=True,
                                        verbose_name="Keltirilgan vaqt haqida izoh")
    average_percentage = models.FloatField(null=True, blank=True, verbose_name="Umumiy sifat foizi")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    def save(self, *args, **kwargs):
        # average_percentage ni hisoblash
        if self.ordered_quantity and self.delivered_quantity:
            self.percent_products = round((self.delivered_quantity / self.ordered_quantity) * 100, 1)
            self.average_percentage = round((self.delivered_quantity / self.ordered_quantity) * 100, 1)
        else:
            self.percent_products = 0
            self.average_percentage = 0

        # percent_time uchun algorithm
        if self.delivered_time and self.agreed_time:
            if self.delivered_time > self.agreed_time:
                self.description_time = "Vaqtida yetib kelmadi"
            else:
                self.description_time = "Vaqtida yetib keldi"

        super(Qualities, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Quality'
        verbose_name_plural = 'Yetkazilgan mahsulotlar sifati'
        db_table = 'quality'

    def __str__(self):
        return self.company.name
