from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Member, MemberAdmin)

class ProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description', 'supplier_id', 'category_id', 'unit', 'price', 'image_tag')
    list_filter = ('product_name', 'supplier_id', 'category_id', 'unit', 'price')
    search_fields = ('product_name', 'supplier_id', 'category_id', 'unit', 'price')

admin.site.register(Products, ProductsAdmin)

class CategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    list_filter = ('category_name', 'description')
    search_fields = ('category_name', 'description')

admin.site.register(Categories, CategoriesAdmin)

class ContactsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_email', 'message')
    list_filter = ('contact_name', 'contact_email', 'message')
    search_fields = ('contact_name', 'contact_email', 'message')

admin.site.register(Contacts, ContactsAdmin)

class ReviewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'product_id', 'customer_name', 'customer_email', 'review', 'rate', 'datetime')
    list_filter = ('id', 'product_id', 'customer_name', 'customer_email', 'review', 'rate',  'datetime')
    search_fields = ('id', 'product_id', 'customer_name', 'customer_email', 'review', 'rate', 'datetime')

admin.site.register(Reviews, ReviewsAdmin)
