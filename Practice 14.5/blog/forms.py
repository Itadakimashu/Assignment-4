from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['pub_date']
    
        widgets = {
            'body' : forms.Textarea(),
        }