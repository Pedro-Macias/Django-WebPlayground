# trasformar en vistas basadas en clases
from django.shortcuts import render

# https://docs.djangoproject.com/en/3.1/ref/class-based-views/base/#django.views.generic.base.TemplateView
from django.views.generic.base import TemplateView


# traformar la funcion en una clase

class HomePageView(TemplateView):
    template_name = "core/home.html"
    # procesar la respuesta de la vista
    def get(self,request, *args , **kwargs):
        return render(request, self.template_name,{'title':'Esta es mi web Playground'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
