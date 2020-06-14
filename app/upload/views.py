from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from .models import Accounts, Company
from .forms import UrlForm, SortForm
from .extra_views import make_tables, parse_fields, get_field, is_empty, make_url
from .lookup import title, category
from .cat_list import cats
from .tables import AccountsTable

def test(request):
    table = AccountsTable(Accounts.objects.values('equity')[:100])
    return render(request, 'test.html', {'table':table})


def index(request):
    cats = [(i, make_url(i)) for i in category]
    context = {'cats': cats}
    return render(request, 'index.html', context)


# view to input data into accounts model
@staff_member_required
def uploadfiles(request):
    URL = None
    form = UrlForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # variable from user text input
        URL = form.cleaned_data['URL']
        # import and run function to import data into Accounts model
        if URL.startswith('http://download.companieshouse.gov.uk/Accounts_'):
            from upload.getaccounts import get_accounts
            get_accounts(URL)
    context = {'form':form,
            'URL':URL}
    return render(request, 'button.html', context)


# (hopefully) generic table view
def tables(request, category):
    order = request.GET.get('order_by', 'companyname')
    tables = make_tables(category=category)
    context = {'titles': tables['titles'],
            'table': tables['body']}
    return render(request, 'tables.html', context)


# view for individual record page
def detail(request, companynumber):
    # check if company exists
    try:
        company = Company.objects.get(pk=companynumber)
    except Company.DoesNotExist:
        raise Http404("Question does not exist")
    # collect fields from the models 
    com_fields = parse_fields(Company._meta.get_fields())
    acc_fields = parse_fields(Accounts._meta.get_fields())
    # output format: [[title, accounts1.title, ... , accountsN.title], ... ]
    info = []
    for f in com_fields:
        info.append([get_field(f), getattr(company, f) or ''])
    # collect all accounts for the selected company, newest first
    accounts = Accounts.objects.filter(companynumber=companynumber).order_by('-accountsdate')
    data = []
    for f in acc_fields:
        data.append([get_field(f)] + [getattr(acc, f) or '' for acc in accounts])
    # filter the output to remove rows that are empty
    filtered_info = [i for i in info if not is_empty(i)]
    filtered_data = [i for i in data if not is_empty(i)]
    context = {'data': filtered_data, 'info': filtered_info}
    return render(request, 'detail.html', context)
