from django.db import models
from django.forms import ModelForm
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=200, label="照片說明", required=True)
    file = forms.ImageField(label="照片檢視")
