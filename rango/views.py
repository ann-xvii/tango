from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': page_list,
                    'boldmessage': 'A bold message indeed.'}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': 'I was told to place a bolder message in the context dict.'}
    return render(request, 'rango/about.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}

    try:
        # try to find a category name slug with the given name
        # if not found, the .get() method raises a DoesNotExist exception
        # so the .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all associated pages
        # filter returns 1 or more model instances
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under the name pages.
        context_dict['pages'] = pages

        # we also add the category object from the database to the context dictionary
        # we'll use this in the template to verify that the category exists
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us
        pass

    return render(request, 'rango/category.html', context_dict)
