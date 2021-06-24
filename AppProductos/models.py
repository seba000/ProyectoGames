from django.forms import ModelForm, TextInput, Textarea
from django.db import models

# Create your models here.

class Marca(models.Model):
    marca = models.CharField(max_length=200)
    class Meta:
        db_table: "marca"
    def __str__(self):
        return u'{0}'.format(self.marca)

class Productos(models.Model):
    descripcion = models.CharField(max_length=500)
    precio= models.IntegerField(max_length=10)
    marca= models.ForeignKey(Marca,on_delete=models.CASCADE)
    '''imagen = models.ImageField(upload_to="juegos", null=True)
    '''
    class Meta:
        db_table: "producto"