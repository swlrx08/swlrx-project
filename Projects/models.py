from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField


class Projects(models.Model):
    image = ImageField(upload_to='media/projects_images')
    title = models.CharField(max_length=10)
    short_description = models.CharField(max_length=200)
    project_content = RichTextUploadingField(blank=True, null=True)
    is_delete = models.BooleanField(verbose_name='حذف شده/حذف نشده  ', null=True)
    slug = models.SlugField(allow_unicode=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
