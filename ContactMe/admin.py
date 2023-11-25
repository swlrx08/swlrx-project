from django.contrib import admin

from ContactMe import models


class ContactMeAdmin(admin.ModelAdmin):
    list_filter = ['email']
    list_display = ['email', 'message', 'is_read']


admin.site.register(models.ContactMe, ContactMeAdmin)
