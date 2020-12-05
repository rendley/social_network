from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'email', 'subject', 'body', 'is_answered')
    search_fields = ('body',)
    list_filter = ('date',)


admin.site.register(Contact, ContactAdmin)