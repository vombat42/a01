from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    link = models.URLField()

    def __str__(self):
        return(self.link[:20])


class Chapter(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return(self.name)


class Entry(models.Model):
    chapter = models.ForeignKey(Chapter, blank=False, null=True, on_delete = models.SET_NULL)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=False)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True, blank=True)
    text = models.TextField()
    links = models.ManyToManyField(Link, blank=True)
    grade = models.SmallIntegerField()
    
    def __str__(self):
        return f"{self.chapter} - {self.user} ({self.date_start})"