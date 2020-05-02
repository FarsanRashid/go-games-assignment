from django.contrib import admin
from .models import Category, Game


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)

