from django.contrib import admin
from Documents import models
from sorl.thumbnail.admin import AdminImageMixin


class DocumentsAdmin(AdminImageMixin, admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title']


admin.site.register(models.Documents, DocumentsAdmin)
