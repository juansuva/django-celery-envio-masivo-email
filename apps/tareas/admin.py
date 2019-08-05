from django.contrib import admin
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin
from .task import send_emails_users

class UserAdmin(UserAdmin):
    actions=['send_emails_actions',]

    def send_emails_actions(self, request, queryset):
        send_emails_users.delay()
        filas_actualizadas= queryset.update(is_staff=True)
        return True

admin.site.unregister(User)
admin.site.register(User,UserAdmin)