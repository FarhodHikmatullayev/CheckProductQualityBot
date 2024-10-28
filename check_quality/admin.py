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
        'id', 'company', 'ordered_quantity', 'delivered_quantity', "percent_products",
        "agreed_time",
        "delivered_time", "average_percentage", "created_at")
    list_filter = ('created_at', 'delivered_time', 'agreed_time')
    search_fields = ('company__name',)
    date_hierarchy = 'created_at'
    fields = (
        'company', 'ordered_quantity', 'delivered_quantity', "percent_products", "quality_description", "agreed_time",
        "delivered_time", "description_time", "average_percentage", "created_at")
    readonly_fields = ('created_at', "percent_products", "description_time", "average_percentage")
