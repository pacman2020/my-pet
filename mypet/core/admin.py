from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('city', 'active', 'user_id')
    list_filter = ('city', 'active')
    search_fields = ('city','city')
