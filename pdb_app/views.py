from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.template import loader

from pdb_app.models import Item, Category


def index(request):
    template = loader.get_template('pdb_app/index.html')
    context = {
        'name': 'sukjsiosan',
        'items': Item.objects.all(),
        'title': 'Programming Database',
        'description': 'A list of your favorite programming languages and tools'
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    template = loader.get_template('pdb_app/detail.html')
    item = get_object_or_404(Item, id=id)
    context = {
        'name': 'sukjsiosan',
        'item': item,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    template = loader.get_template('pdb_app/categories.html')
    categories_list: object = Category.objects.all()
    context = {
        'categories': categories_list,
    }
    return HttpResponse(template.render(context, request))
