from django.forms.forms import Form
from django.shortcuts import redirect, render
from AppProductos.models import *
from AppProductos.forms import ProductoForm
# Create your views here.
def home(request):
    return render(request,'index.html')

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
def editar(request,id_producto):
    prod = Productos.objects.get(id=id_producto)
    form = ProductoForm(instance=prod)
    return render(request,'producto_edit.html',{'form': form,'id_producto':id_producto})

#metodo para actualizar datos en bd
def update(request,id_producto):
    prod = Productos.objects.get(id=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('/productos')

#metodo para eliminar un prod
def delete(request,id_producto):
    prod = Productos.objects.get(id=id_producto)
    prod.delete()
    return redirect('/productos')