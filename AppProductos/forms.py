from django import forms
from django.db import models
from django.forms import fields
from AppProductos.models import Marca, Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"