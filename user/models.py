from django.db import models


class User(models.Model):
    login_id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.login_id
