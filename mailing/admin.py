from django.contrib import admin
from .models import Client, Message, Mailing, MailingAttempt


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment')
    list_filter = ('full_name',)
    search_fields = ('email', 'comment')


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ('id', 'subject', 'body')
    search_fields = ('subject', 'body')


@admin.register(Mailing)
class AdminMailing(admin.ModelAdmin):
    list_display = ('id', 'start_at', 'end_at', 'status', 'message', 'show_recipients')
    list_filter = ('status', 'start_at')
    search_fields = ('status',)

    def show_recipients(self, obj):
        return ", ".join(client.email for client in obj.recipients.all())

    show_recipients.short_description = "Получатели"


@admin.register(MailingAttempt)
class AdminMailingAttempt(admin.ModelAdmin):
    list_display = ('id', 'attempt_time', 'status', 'mailing', 'server_response')
    list_filter = ('status', 'attempt_time')
    search_fields = ('status',)
