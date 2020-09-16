from django import forms
from .models import News


class NewsForm(forms.Form):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
