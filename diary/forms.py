from django import forms
from hello.models import mTextfile
from django.forms import ModelForm

class fNameAge(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()

class fUpFile(forms.ModelForm):
    class Meta:
        model = mTextfile
        fields = ('textfile', )
