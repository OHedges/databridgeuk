from django import forms

class UrlForm(forms.Form):
    URL = forms.CharField(label='URL', max_length=200)
