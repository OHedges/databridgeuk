from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UrlForm

def uploadfiles(request):
    URL = False
    form = UrlForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        URL = form.cleaned_data['URL']
    context = {'form':form,
            'URL':URL,
            }
    return render(request, 'button.html', context)

