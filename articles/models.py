from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_now = models.DateTimeField(auto_now_add=True)
    updated_now = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)