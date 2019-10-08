from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        title = forms.CharField(max_length=100)
        fields = ['cover', 'title']