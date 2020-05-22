from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UrlForm

def uploadfiles(request):
    URL = False
    form = UrlForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # variable from user text input
        URL = form.cleaned_data['URL']

        # import and run function to import data into Accounts model
        if URL.startswith('http://download.companieshouse.gov.uk/Accounts_'):
            from upload.getaccounts import get_accounts
            get_accounts(URL)

    context = {'form':form,
            'URL':URL,
            }
    return render(request, 'button.html', context)

