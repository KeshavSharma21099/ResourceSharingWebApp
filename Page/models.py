from django.db import models
from django.contrib.auth.models import User
from Directory.models import Directory


class Page(models.Model):
    user = models.ForeignKey(User, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    link = models.URLField()
    directory = models.ForeignKey(Directory, related_name='pages', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username + ": " + self.title
