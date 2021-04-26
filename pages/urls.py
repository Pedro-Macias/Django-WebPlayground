from django.urls import path
# en vez de cargar una vista basada en funciones , importamos la clase
from .views import PagesListView , PagesDetailView
urlpatterns = [
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
]