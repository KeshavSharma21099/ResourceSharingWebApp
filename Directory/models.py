from django.db import models
from django.contrib.auth.models import User


class Directory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)

    def __str__(self):
        return self.name
