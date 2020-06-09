from django import forms
from .models import Photo


class ImgForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'Img']
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
             'Img' : forms.FileInput(attrs={'class': 'custom-file', 'class': 'input-group'}),

        }