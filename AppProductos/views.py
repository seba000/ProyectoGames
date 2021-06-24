from django.contrib.auth.models import User
from django.forms import forms
from django.forms.forms import Form
from django.shortcuts import redirect, render
from AppProductos.models import *
from AppProductos.forms import ProductoForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'index.html')
@login_required(login_url='login')
def producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/productos')
            except:
                pass
    else:
        form = ProductoForm()
        productos = Productos.objects.all()
        return render(request, 'productos.html',{'form': form,'productos':productos})

#metodo para editar
@login_required(login_url='login')
def editar(request,id_producto):
    prod = Productos.objects.get(id=id_producto)
    form = ProductoForm(instance=prod)
    return render(request,'producto_edit.html',{'form': form,'id_producto':id_producto})

#metodo para actualizar datos en bd
@login_required(login_url='login')
def update(request,id_producto):
    prod = Productos.objects.get(id=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('/productos')

#metodo para eliminar un prod
@login_required(login_url='login')
def delete(request,id_producto):
    prod = Productos.objects.get(id=id_producto)
    prod.delete()
    return redirect('/productos')

#metodo para crear usuarios
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/productos')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Se a creado el usuario exitosamente '+ user)
                return redirect('/login')
        return render(request,'register.html',{'form':form})

#metodo para iniciar sesion
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/productos')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/productos')
            else:
                messages.info(request,'Usuario o password incorrectos')
        return render(request,'login.html',{})

def logoutUser(request):
    logout(request)
    return redirect('login')