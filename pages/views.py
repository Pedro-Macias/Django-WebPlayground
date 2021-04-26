
from .models import Page
from django.urls import reverse, reverse_lazy
# importamos listviews
from django.views.generic.list import ListView
# importamos dateilviews
from django.views.generic.detail import DetailView
# importarmos Createviews
from django.views.generic.edit import CreateView


# Create your views here.

# UTILIZAR LIST VIEWS
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#django.views.generic.list.ListView
# Devolver una lista generica y devolverla en un template

class PagesListView(ListView):
    model = Page

# UTILIZAR DETAIL VIEW 
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView
class PagesDetailView(DetailView):
    model = Page

# UTILIZAR CREATE VIEWS
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
class PagesCreate(CreateView):
    model = Page
    # que campos queremos que edite el usuario
    fields = ['title','content','order']
    # funcion get_success_url para retornar el valor
    ''' def get_success_url(self):
            return reverse('pages:pages')'''
    # podemos sustituir la fucion por un reverse_lazy
    success_url = reverse_lazy ('pages:pages')
