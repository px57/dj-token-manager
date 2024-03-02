from django.contrib import admin
from token_manager import models

@admin.register(models.TokenModels)
class TokenAdmin(admin.ModelAdmin):
    list_display = (
        'token',
        'profile',
        'is_active',
        'number_of_uses',
        'relatedModel',
        'label',
    )