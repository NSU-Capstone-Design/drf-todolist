from django.utils import timezone
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('user.User', related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    checked = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='todos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
