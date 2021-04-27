
from .models import Page
from django.urls import reverse, reverse_lazy
# importamos listviews
from django.views.generic.list import ListView
# importamos dateilviews
from django.views.generic.detail import DetailView
# importarmos Createviews
from django.views.generic.edit import CreateView
# importamos UpdateView
from django.views.generic.edit import UpdateView


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

# UTILIZAR CREATE VIEWS para crear paginas
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
class PagesCreate(CreateView):
    model = Page
    # que campos queremos que edite el usuario
    fields = ['title','content','order']
    # funcion get_success_url para retornar el valor
    ''' def get_success_url(self):
            return reverse('pages:pages')'''
    # podemos sustituir la funcion por un reverse_lazy
    success_url = reverse_lazy ('pages:pages')

# UTILIZAR UPDATE VIEWS , para editar paginas 
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView
class PagesUpdate(UpdateView):
# necesitamos pasarle 3 campos , el modelo  y el subfijo para que vaya a buscar el template
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return  reverse_lazy('pages:update',args=[self.object.id]) + '?ok'
