from django.contrib import admin
from .models import Game, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}  # Automatically fill the slug
