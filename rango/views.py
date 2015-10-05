from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'I am bold font from the context!!!'}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("<h1>Rango says, 'This is the about page!!'</h1><br/><p><a href='/rango'>Back!</a></p>")
