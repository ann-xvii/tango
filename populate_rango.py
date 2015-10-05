"""
Population script for the database
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat(name='Python', views=128, likes=64)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/",
             views=12)

    add_page(cat=python_cat,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/",
             views=14)

    add_page(cat=python_cat,
             title="Learn Python in 10 Min",
             url="http://www.korokithakis.net/tutorials/python/",
             views=21)

    django_cat = add_cat(name="Django", views=64, likes=32)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.8/intro/tutorial01/",
             views=24)

    add_page(cat=django_cat,
             title="Backwards Incompatible Changes in Django 1.8",
             url="https://docs.djangoproject.com/en/1.8/releases/1.8/#backwards-incompatible-changes-in-1-8",
             views=20)

    add_page(cat=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/",
             views=39)

    add_page(cat=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/",
             views=14)

    frame_cat = add_cat(name="Other Frameworks", views=32, likes=16)

    add_page(cat=frame_cat,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/",
             views=10)

    add_page(cat=frame_cat,
             title="Flask",
             url="http://flask.pocoo.org",
             views=10)

    # Print out what we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    return c


# Start execution here! Exclude if imported
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()