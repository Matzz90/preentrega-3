from django.urls import path
from applibros import views
#from AppCoder import curso
#views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor', views.autor, name="Autor"),
    path('genero', views.genero, name="Genero"),
    path('libro', views.libro, name="Libro"),
]
    