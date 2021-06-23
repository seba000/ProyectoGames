from django.http import HttpResponse
from django.template import Template, context, loader
def holaMUndo(request):
    return HttpResponse("<h1>Hola primer Django</h1>")

def template(request,usu):
    usuario= usu
    libros = ["juego de tronos","el problema de 3","el bosque oscuro","jhon wick"]
    temp = loader.get_template('index.html')
    pag = temp.render({"nombre_usuario":usu,"libros":libros})
    return HttpResponse(pag)
    