from django.contrib import admin

from .models import *


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'username', 'role', 'joined_at')
    list_filter = ('joined_at', 'role')
    search_fields = ('full_name', 'username', 'role')
    date_hierarchy = 'joined_at'


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Qualities)
class QualitiesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company', 'ordered_quantity', 'delivered_quantity', "percent_products", "invalid_quantity",
        "agreed_time",
        "delivered_time", "percent_time", "percentage_quality", "average_percentage", "created_at")
    list_filter = ('created_at', 'delivered_time', 'agreed_time')
    search_fields = ('company__name',)
    date_hierarchy = 'created_at'
    fields = ('company', 'ordered_quantity', 'delivered_quantity', "invalid_quantity", "agreed_time", "delivered_time")
