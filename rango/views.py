from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list,
                    'boldmessage': 'A bold message indeed.'}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': 'I was told to place a bolder message in the context dict.'}
    return render(request, 'rango/about.html', context_dict)
