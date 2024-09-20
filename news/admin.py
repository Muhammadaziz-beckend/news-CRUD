from django.contrib import admin
from .models import *



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name','data_add','data_now','is_public']
    list_display_links = ['id','name','data_add','data_now']
    list_editable = ['is_public']
    list_filter = ['category','tags']

    ordering = ['data_add']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name','data_add','data_now']
    list_display_links = ['id','name','data_add','data_now']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','data_add','data_now']
    list_display_links = ['id','name','data_add','data_now']
