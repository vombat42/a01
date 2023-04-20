from django.db import models
#from django.forms import ModelForm

class mTextfile(models.Model):
    textfile = models.FileField(upload_to='userfiles/', verbose_name="Выберите файл")
