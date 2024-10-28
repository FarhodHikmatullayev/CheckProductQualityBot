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
    company = models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kompaniya")
    ordered_quantity = models.IntegerField(null=True, blank=True, verbose_name="Zakaz qilingan mahsulotlar soni")
    delivered_quantity = models.IntegerField(null=True, blank=True, verbose_name="Keltirilgan mahsulotlar soni")
    percent_products = models.FloatField(null=True, blank=True,
                                         verbose_name="Kelishilgan mahsulotlarning yetkazib berilganlik foizi")
    invalid_quantity = models.IntegerField(null=True, blank=True, verbose_name="Yaroqsiz mahsulotlar soni")
    agreed_time = models.DateTimeField(null=True, blank=True, verbose_name="Yetkazib berish kelishilgan vaqt")
    delivered_time = models.DateTimeField(null=True, blank=True, verbose_name="Yetkazib berilgan vaqt")
    percent_time = models.FloatField(null=True, blank=True, verbose_name="Kelishilgan vaqtda yetkazib berilish foizi")
    percentage_quality = models.FloatField(null=True, blank=True, verbose_name="Yetkazilgan Mahsulotlar sifati foizi")
    average_percentage = models.FloatField(null=True, blank=True, verbose_name="Umumiy sifat foizi")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    def save(self, *args, **kwargs):
        # average_percentage ni hisoblash
        if self.ordered_quantity and self.delivered_quantity:
            self.percent_products = (self.delivered_quantity / self.ordered_quantity) * 100
        else:
            self.percent_products = 0

        # percent_time uchun algorithm
        """percent_time uchun kod yozing"""

        # percentage_quality uchun algorithm
        if self.delivered_quantity and self.invalid_quantity:
            # Qo'shimcha mahsulotlar sifatini hisoblash uchun matematik ifoda
            valid_quantity = self.delivered_quantity - self.invalid_quantity
            if valid_quantity > 0:
                self.percentage_quality = (valid_quantity / self.delivered_quantity) * 100
            else:
                self.percentage_quality = 0
        else:
            self.percentage_quality = 0

        # average_percentage ni hisoblash
        """average_percentage ni hisoblash algorithmini yozing"""

        super(Qualities, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Quality'
        verbose_name_plural = 'Yetkazilgan mahsulotlar sifati'
        db_table = 'quality'

    def __str__(self):
        return self.company.name
