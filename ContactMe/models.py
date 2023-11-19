from django.db import models


class ContactMe(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.email