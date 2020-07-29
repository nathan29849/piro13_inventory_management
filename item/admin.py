from django.contrib import admin
from .models import Account, Item

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

