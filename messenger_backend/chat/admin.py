from django.contrib import admin
from .models import Chat, Message

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chat_picture')
    search_fields = ('id', 'name', 'chat_picture')

    def chat_name(self, obj):
        return obj.chat.name


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'text')
    search_fields = ('id', 'from_user', 'text')


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)