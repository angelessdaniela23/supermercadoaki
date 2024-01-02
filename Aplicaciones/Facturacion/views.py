from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.
def listadoClientes(request):
    clientesBdd=Cliente.objects.all()
    return render(request, 'listadoClientes.html', {'clientes':clientesBdd})


def guardarCliente(request):
    cedula=request.POST["cedula"]
    apellido=request.POST["apellido"]
    nombre=request.POST["nombre"]
    direccion=request.POST["direccion"]
    fecha_nacimiento=request.POST["fecha_nacimiento"]
    correo=request.POST["correo"]
    #Insertando datos mediante el ORM de django
    cliente =Cliente.objects.create(cedula=cedula,apellido=apellido,nombre=nombre,direccion=direccion,fecha_nacimiento=fecha_nacimiento,correo=correo)
    return redirect('/')


def eliminarCliente(request,id):
    clienteEliminar=Cliente.objects.get(id=id)
    clienteEliminar.delete()
    return redirect('/')

# paginas 

def tu_sazon(request):
    # Lógica de la vista
    return render(request, 'tu_sazon.html')

def tu_comunidad(request):
    # Lógica de la vista
    return render(request, 'tu_comunidad.html')
def club(request):
    # Lógica de la vista
    return render(request, 'club.html')
def producto_aki(request):
    # Lógica de la vista
    return render(request, 'producto_aki.html')
def la_original(request):
    # Lógica de la vista
    return render(request, 'la_original.html')