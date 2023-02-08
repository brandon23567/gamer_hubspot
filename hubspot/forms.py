from django import forms
from django.forms import ModelForm, widgets      
from cloudinary.forms import CloudinaryFileField      
from .models import UploadVideo

class UploadVideoForm(ModelForm):
  class Meta:
    model = UploadVideo
    fields = "__all__"
    widgets={
      'title' : forms.TextInput(attrs={'class':'form-control'}),
    }