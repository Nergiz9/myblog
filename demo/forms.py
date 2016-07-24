from django import forms
from demo.models import Post

__author__ = 'nergiz'


class CommentForm(forms.Form):
    author = forms.CharField(max_length=60)
    mail = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
