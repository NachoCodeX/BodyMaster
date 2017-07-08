from django.db import models

# Create your models here.
class Articulo(models.Model):
    TYPES=(
        (1,'PROTEINAS'),(2,'OXIDOS'),
        (3,'QUEMADORES'),(4,'GANADORES'),
        (5,'CREATINAS'),(6,'GLUTAMINAS'),
        (7,'CARNITINAS'),(8,'CLS'),
        (9,'PRECURSORES'),(10,'MULTIVITAMINICOS'),
        (11,'ACCESORIOS'),(12,'BCCAS'),(13,'AMINOACIDOS'),
    )

    nombre = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    cantidad = models.PositiveSmallIntegerField(default=0)
    tipo = models.PositiveSmallIntegerField(blank=True, null=True, choices=TYPES)
    img = models.ImageField(upload_to="imagenes/", null=True,blank=True,default='/imagenes/default.png')
    dec = models.TextField(blank=True)
    # ##################
    codigo_de_barras = models.CharField(blank=True,null=True, max_length=120)

    def __str__(self):
        return self.nombre
