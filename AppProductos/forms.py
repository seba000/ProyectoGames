from django import forms
from django.db import models
from django.forms import fields
from AppProductos.models import Marca, Productos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']