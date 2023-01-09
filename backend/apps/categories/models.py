from django.db import models

class Category(models.Model):
    name = models.CharField(
        'Name', blank=False, null=False, max_length=100
    )
    color_code = models.CharField(
        'Color Code', blank=False, null=False, max_length=50
    )
    created_at = models.DateTimeField(
        'Creation Date', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Update Date', blank=True, auto_now=True
    )

    def __str__(self):
        return self.name