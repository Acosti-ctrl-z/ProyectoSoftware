"""
URL configuration for Super project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Controlador.ControladorUsuario import PerfilController
from Controlador.ControladorMedicamentos import MedicamentoContrller
from Controlador.ControladorFarmacia import FarmaciaController
from Controlador.ControladorLaboratorio import LaboratorioController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PerfilController.home, name='home'),
    path('signup/', PerfilController.signup, name='signup'),
    path('perfiles/', PerfilController.perfiles, name='perfiles'),
    path('logout/', PerfilController.signout, name='signout'),
    path('signin/', PerfilController.signin, name='signin'),
    path('registrar/', MedicamentoContrller.registrar_medicamento, name='registrar_medicamento'),
    path('lista/', MedicamentoContrller.lista_medicamentos, name='lista_medicamentos'),
    path('labs/', LaboratorioController.labs, name='labs'),
    path('crear_labs/', LaboratorioController.crear_labs, name='crear_labs'),

    path('registro_farm/', FarmaciaController.registrar_farmacia, name='agregar_farmacia'),
    path('lista_farm/', FarmaciaController.lista_farm, name='lista_farmacias'),
]
