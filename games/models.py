from django.db import models

path='games/'
#path=''

class Chapter(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} - {self.id}"


class Letter(models.Model):
    name = models.CharField(max_length=1, unique=True)
    voice = models.FileField(upload_to=f'{path}voice', blank=True, null=True)
    # letter_outline = models.ImageField(upload_to=f'{path}img/outline/', blank=True, null=True)
    # letter_black = models.ImageField(upload_to=f'{path}img/black/', blank=True, null=True)
    # letter_color = models.ImageField(upload_to=f'{path}img/color/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.id}"


class Word(models.Model):
    chapter = models.ForeignKey(Chapter, blank=False, null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=10, unique=True)
    voice = models.FileField(upload_to=f'{path}voice')
    letters=models.ManyToManyField(Letter, blank=False)
    
    def __str__(self):
        return f"{self.chapter} - {self.name}"