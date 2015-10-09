from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from simpletab.models import Tab_model

def index(request):
    table_list = Tab_model.objects.order_by('-texts_field')[:5]
    output = ', '.join([p.text_field for p in table_list])
    return HttpResponse(output)

def detail(request, simpletab_id):
    return HttpResponse('hello detail %s.' % simpletab_id)

def result(request, simpletab_id):
    response = 'Hello result %s.'
    return HttpResponse(response % simpletab_id)

def vote(request, simpletab_id):
    return HttpResponse('hello vote %s.' % simpletab_id)
