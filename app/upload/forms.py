from django import forms
from .extra_views import mach_titles
from .lookup import title

class UrlForm(forms.Form):
    URL = forms.CharField(label='URL', max_length=200)

class SortForm(forms.Form):
    sortby = forms.ChoiceField(choices=[(i, title.get(i, i)) for i in mach_titles])
    direction = forms.ChoiceField(choices=[('ascending','ascending'),('descending','descending')])

