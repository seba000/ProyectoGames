"""ProyectoGames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from ProyectoGames.settings import MEDIA_ROOT
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import logout
from django.urls import path
from django.conf.urls.static import static
from AppProductos import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('index/',views.home),
    path('productos/',views.producto,name="productos"),
    path('edit/<int:id_producto>',views.editar),
    path('update/<int:id_producto>',views.update),
    path('delete/<int:id_producto>',views.delete),

    #urls para los usuarios
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)