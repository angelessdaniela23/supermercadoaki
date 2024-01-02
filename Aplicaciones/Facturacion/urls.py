from django.urls import path
from . import views

urlpatterns=[
    path('',views.listadoClientes),
    path('guardarCliente/',views.guardarCliente),
    path('eliminarCliente/<id>',views.eliminarCliente)
]
