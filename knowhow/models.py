from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20, unique=True)
    rank = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.rank}"

class Chapter(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return(self.name)

class Article(models.Model):
    name = models.CharField(max_length=50, unique=True)
    chapter = models.ForeignKey(Chapter, null=True, on_delete = models.SET_NULL)
    description = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete = models.PROTECT)
    date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.author}"

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete = models.PROTECT)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.article} - {self.author}"
