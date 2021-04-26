
from .models import Page
# importamos listviews
from django.views.generic.list import ListView
# importamos dateilviews
from django.views.generic.detail import DetailView

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