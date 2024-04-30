from django.shortcuts import render, redirect, HttpResponse
from main.models import Cliente, Productos
from main.forms import AddCliente, AddProducto
from POS.models import Article
from django.http import JsonResponse
from django.db.models import Q
from django.views.generic import ListView
from django.template.loader import get_template
from django.conf import settings
import os

def POS(request):
    articulo = Article.objects.all()
    clientes = Cliente.objects.all()

    return render(request, 'POScopy.html', {
        'title':'Punto de Venta',
        'clientes': clientes,
        'articulo': articulo,
    })

def clientes_view(request):
    clientes = Cliente.objects.all()

    return render(request, 'clientes.html', {
        'title':'Clientes',
        'clientes' : clientes
    })

def productos_view(request):
    productos = Productos.objects.all()

    return render(request, 'productos.html', {
        'title':'Productos',
        'productos' : productos
    })

def add_producto_view(request):

    context={}

    if request.method == 'POST':

        estado=False

        description = request.POST['description']
        codigo = request.POST['codigo']
        Unidad_Compras = request.POST['Unidad_Compras']
        Unidad_Ventas = request.POST['Unidad_Ventas']
        Unidad_Inventario = request.POST['Unidad_Inventario']
        cantidad_Unidad_Compras = request.POST['cantidad_Unidad_Compras']
        Cto_Unidad_Compras = request.POST['Cto_Unidad_Compras']
        Porc_GastosVarios = request.POST['Porc_GastosVarios']
        Porc_impuestos = request.POST['Porc_impuestos']

        producto = Productos(
            description = description,
            codigo = codigo,
            Unidad_Compras = Unidad_Compras,
            Unidad_Ventas = Unidad_Ventas,
            Unidad_Inventario = Unidad_Inventario,
            cantidad_Unidad_Compras = cantidad_Unidad_Compras,
            Cto_Unidad_Compras = Cto_Unidad_Compras,
            Porc_GastosVarios = Porc_GastosVarios,
            Porc_impuestos = Porc_impuestos
        )

        producto.save()
        estado=True

        context = {'estado':estado}
        return redirect('Productos')

    return render(request, 'add_producto.html', context)



def delete_producto_view(request, id):
    articulo = Productos.objects.get(pk=id)
    articulo.delete()

    return redirect('Productos')

def add_cliente_view(request):

    if request.method == 'POST':
        formulario = AddCliente(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            razon = data_form['razon']
            rfc = data_form['rfc']
            credito = data_form['credito']
            limite_credito = data_form['limite_credito']
            dias_credito = data_form['dias_credito']
            lista_precios = data_form['lista_precios']
            nombre_comercial = data_form['nombre_comercial']
            dirEstado = data_form['dirEstado']
            dirCiudad = data_form['dirCiudad']
            dirColonia = data_form['dirColonia']
            dircalle = data_form['dircalle']
            dirnumext = data_form['dirnumext']
            dirnumint = data_form['dirnumint']
            telefono = data_form['telefono']

            cliente = Cliente(
                razon = razon,
                rfc = rfc,
                credito = credito,
                limite_credito = limite_credito,
                dias_credito = dias_credito,
                lista_precios = lista_precios,
                nombre_comercial = nombre_comercial,
                dirEstado = dirEstado,
                dirCiudad = dirCiudad,
                dirColonia = dirColonia,
                dircalle = dircalle,
                dirnumext = dirnumext,
                dirnumint = dirnumint,
                telefono = telefono
            )
        
            cliente.save()
            return redirect('Clientes')

    else:
        formulario = AddCliente()

    return render(request, 'add_clientes.html', {
        'form' : formulario
    })

def edit_cliente_view(request, id):
    """cliente = Cliente.objects.get(pk=id)
    cliente.save()
    return redirect('Clientes')"""
    pass

def delete_cliente_view(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()

    return redirect('Clientes')

def get_data(request):
    data = Cliente.objects.values()
    return JsonResponse(list(data), safe=False)

def buscar_cliente(request):
    query = request.GET.get('q', '')
    
    if query:
        resultados = Cliente.objects.filter(razon__icontains=query)
    else:
        resultados= []

    return render(request, 'POS.html', {
        'query': query,
        'resultados':resultados,
        })

def buscar_producto(request):
    query = request.GET.get('p', '')
    
    if query:
        resultado = Article.objects.filter(description__icontains=query)
    else:
        resultado= []

    return render(request, 'POS.html', {
        'query': query,
        'resultado':resultado,
        })

def seleccionar(request, id):
    elemento_seleccionado = Article.objects.get(pk=id)
    return render(request, 'POS.html', {'elemento_seleccionado': elemento_seleccionado})

def venta(request):
    return render(request, 'venta.html')


def editar_producto(request, id):
    if request.method == 'GET':
        producto = Productos.objects.get(pk=id)
        return render(request, 'editar.html', {'producto': producto})
    return redirect('Productos')
    

def actualizar_producto(request, id):
    if request.method == 'POST':
        producto = Productos.objects.get(pk=id)
        
        producto.description = request.POST['description']
        producto.codigo = request.POST['codigo']
        producto.Unidad_Compras = request.POST['Unidad_Compras']
        producto.Unidad_Ventas = request.POST['Unidad_Ventas']
        producto.Unidad_Inventario = request.POST['Unidad_Inventario']
        producto.cantidad_Unidad_Compras = request.POST['cantidad_Unidad_Compras']
        producto.Cto_Unidad_Compras = request.POST['Cto_Unidad_Compras']
        producto.Porc_GastosVarios = request.POST['Porc_GastosVarios']
        producto.Porc_impuestos = request.POST['Porc_impuestos']
        producto.Cto_Factura= request.POST['Cto_Factura']
        producto.Cto_Integrado= request.POST['Cto_Integrado']

        producto.save()

        
        return redirect('Productos')
        
