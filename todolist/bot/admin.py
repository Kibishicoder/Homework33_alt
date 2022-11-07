from django.contrib import admin

from bot.models import TgUser


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'user_id', 'user')
    read_only_fields = ('chat_id', 'verification_code')

