from django.contrib import admin
from Documents import models


class DocumentsAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title']


admin.site.register(models.Documents, DocumentsAdmin)
