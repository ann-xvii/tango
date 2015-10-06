from django.conf.urls import url
from registration.backends.simple.views import RegistrationView
from rango import views


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):

    def get_success_url(self, request, user):
        return '/rango/'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^restricted/', views.restricted, name='restricted'),
]
