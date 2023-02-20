from django.shortcuts import render
from .models import Libro

def inicio(request):
    return render(request, 'applibros/inicio.html')
    
def autor(request):
    return render(request, 'applibros/autor.html')
    
def genero(request):
    return render(request, 'applibros/genero.html')
    
def libro(request):
    return render(request, 'applibros/libro.html')
    
    
    
