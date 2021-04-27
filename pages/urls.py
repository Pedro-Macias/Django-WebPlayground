from django.urls import path
# en vez de cargar una vista basada en funciones , importamos la clase
from .views import PagesListView , PagesDetailView, PagesCreate, PagesUpdate, PagesDelete

# busqueda reversa de las vistas
pages_patterns =( [
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
    path('create/', PagesCreate.as_view(), name='create'),
    path('update/<int:pk>/', PagesUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PagesDelete.as_view(), name='delete'),
],'pages')