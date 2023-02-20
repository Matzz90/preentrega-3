from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    descripcion = models.TextField()
    generos = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo
