from django.shortcuts import render, redirect, HttpResponse
from main.models import Cliente, Productos
from main.models import Proveedor, Marca, Familia, UnidadMedida, Moneda
from main.forms import AddCliente, AddProducto
from POS.models import Article
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

"""def add_producto_view(request):

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

    return render(request, 'add_producto.html', context)"""

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
    pass

def delete_cliente_view(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()

    return redirect('Clientes')

"""def editar_producto(request, id):
    if request.method == 'GET':
        producto = Productos.objects.get(pk=id)
        return render(request, 'editar.html', {'producto': producto})
    return redirect('Productos')"""
    

"""def actualizar_producto(request, id):
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

        
        return redirect('Productos')"""


def add_producto_view(request, producto_id=None):
    unidadmedida = UnidadMedida.objects.all()
    moneda = Moneda.objects.all()
    
    if producto_id:
        producto = Productos.objects.get(id=producto_id)
        action = 'Editar Producto'
        title = 'Editar Producto'
    else:
        producto = None
        action = 'Nuevo Producto'
        title = 'Nuevo Producto'

    if request.method == 'POST':

        _description = request.POST['description']
        _codigo = request.POST['codigo']
        _Unidad_Compras = request.POST['Unidad_Compras']
        _Unidad_Ventas = request.POST['Unidad_Ventas']
        _Unidad_Inventario = request.POST['Unidad_Inventario']
        _cantidad_Unidad_Compras = request.POST['cantidad_Unidad_Compras']
        _Cto_Unidad_Compras = request.POST['Cto_Unidad_Compras']
        _Porc_GastosVarios = request.POST['Porc_GastosVarios']
        _Porc_impuestos = request.POST['Porc_impuestos']
        _moneda = request.POST['moneda']
        _t_cambio = request.POST['t_cambio']
        _precio1 = request.POST['precio1']
        _precio2 = request.POST['precio2']
        _precio3 = request.POST['precio3']
        _precio4 = request.POST['precio4']
        _precio5 = request.POST['precio5']
        _porc_util_1 = request.POST['porc_util_1']
        _porc_util_2 = request.POST['porc_util_2']
        _porc_util_3 = request.POST['porc_util_3']
        _porc_util_4 = request.POST['porc_util_4']
        _porc_util_5 = request.POST['porc_util_5']
        _precioMN1 = request.POST['precioMN1']
        _precioMN2 = request.POST['precioMN2']
        _precioMN3 = request.POST['precioMN3']
        _precioMN4 = request.POST['precioMN4']
        _precioMN5 = request.POST['precioMN5']
        _codigo_prov = request.POST['codigo_prov']
        _codigo_barras = request.POST['codigo_barras']

        if producto:
            producto.description = request.POST['description']
            producto.codigo = request.POST['codigo']
            producto.Unidad_Compras = request.POST.get('Unidad_Compras')
            producto.Unidad_Ventas = request.POST['Unidad_Ventas']
            producto.Unidad_Inventario = request.POST['Unidad_Inventario']
            producto.cantidad_Unidad_Compras = request.POST['cantidad_Unidad_Compras']
            producto.Cto_Unidad_Compras = request.POST['Cto_Unidad_Compras']
            producto.Porc_GastosVarios = request.POST['Porc_GastosVarios']
            producto.Porc_impuestos = request.POST['Porc_impuestos']
            producto.Cto_Factura= request.POST['Cto_Factura']
            producto.Cto_Integrado= request.POST['Cto_Integrado']
            producto.moneda= request.POST['moneda']
            producto.t_cambio= request.POST['t_cambio']
            producto.precio1= request.POST['precio1']
            producto.precio2= request.POST['precio2']
            producto.precio3= request.POST['precio3']
            producto.precio4= request.POST['precio4']
            producto.precio5= request.POST['precio5']
            producto.precioMN1= request.POST['precioMN1']
            producto.precioMN2= request.POST['precioMN2']
            producto.precioMN3= request.POST['precioMN3']
            producto.precioMN4= request.POST['precioMN4']
            producto.precioMN5= request.POST['precioMN5']
            producto.codigo_prov= request.POST['codigo_prov']
            producto.codigo_barras = request.POST['codigo_barras']
            producto.save()
        else:
            Productos.objects.create(description=_description,
                                     codigo=_codigo,
                                     Unidad_Compras=_Unidad_Compras,
                                     Unidad_Ventas = _Unidad_Ventas,
                                     Unidad_Inventario=_Unidad_Inventario,
                                     cantidad_Unidad_Compras = _cantidad_Unidad_Compras,
                                     Cto_Unidad_Compras=_Cto_Unidad_Compras,
                                     Porc_GastosVarios=_Porc_GastosVarios,
                                     Porc_impuestos=_Porc_impuestos,
                                     moneda= _moneda,
                                     t_cambio= _t_cambio,
                                     precio1=_precio1,
                                     precio2=_precio2,
                                     precio3=_precio3,
                                     precio4=_precio4,
                                     precio5=_precio5,
                                     porc_util_1=_porc_util_1,
                                     porc_util_2=_porc_util_2,
                                     porc_util_3=_porc_util_3,
                                     porc_util_4=_porc_util_4,
                                     porc_util_5=_porc_util_5,
                                     precioMN1 = _precioMN1,
                                     precioMN2 = _precioMN2,
                                     precioMN3 = _precioMN3,
                                     precioMN4 = _precioMN4,
                                     precioMN5 = _precioMN5,
                                     codigo_prov=_codigo_prov,
                                     codigo_barras=_codigo_barras,
                                     )
        

        return redirect('Productos')    

    return render(request, 'add_producto.html',{
        'producto': producto, 
        'action': action,
        'unidad': unidadmedida,
        'moneda': moneda,
        'title':title})

def marca_view(request):
    marca = Marca.objects.all()

    return render(request, 'marca.html', {
        'marca' : marca,
        'title' : 'Marca'
    })

def add_marca_view(request, marca_id=None):

    if marca_id:
        marca = Marca.objects.get(id=marca_id)
        action = 'Editar Marca'
    else:
        marca = None
        action = 'Nueva Marca'

    if request.method == 'POST':
        _description = request.POST['description']
        
        if marca:
            marca.description = request.POST['description']
            marca.save()
        else:
            Marca.objects.create(description=_description)

        return redirect('Marca') 
    return render(request, 'add_marca.html',{
        'marca' : marca,
        'action' : action,
    })

def delete_marca(request, id):
    marca = Marca.objects.get(pk=id)
    marca.delete()

    return redirect('Marca')

def proveedor_view(request):
    proveedor = Proveedor.objects.all()

    return render(request, 'proveedor.html', {
        'proveedor' : proveedor,
        'title': 'Proveedor'
    })

def add_proveedor_view(request, proveedor_id=None):
    if proveedor_id:
        proveedor = Proveedor.objects.get(id=proveedor_id)
        action = 'Editar Proveedor'
    else:
        proveedor = None
        action = 'Nuevo Proveedor'

    if request.method == 'POST':
        _description = request.POST['description']
        
        if proveedor:
            proveedor.description = request.POST['description']
            proveedor.save()
        else:
            Proveedor.objects.create(description=_description)

        return redirect('Proveedor') 
    return render(request, 'add_proveedor.html',{
        'proveedor' : proveedor,
        'action' : action,
    })

def delete_proveedor(request, id):
    proveedor = Proveedor.objects.get(pk=id)
    proveedor.delete()

    return redirect('Proveedor')

def familia_view(request):
    familia = Familia.objects.all()

    return render(request, 'familia.html', {
        'familia' : familia,
        'title': 'Familia'
    })

def add_familia_view(request, familia_id=None):
    if familia_id:
        familia = Familia.objects.get(id=familia_id)
        action = 'Editar Familia'
    else:
        familia = None
        action = 'Nueva Familia'

    if request.method == 'POST':
        _description = request.POST['description']
        
        if familia:
            familia.description = request.POST['description']
            familia.save()
        else:
            Familia.objects.create(description=_description)

        return redirect('Familia') 

    return render(request, 'add_familia.html',{
        'familia': familia,
        'action' : action,
    })

def delete_familia(request, id):
    familia = Familia.objects.get(pk=id)
    familia.delete()

    return redirect('Familia')

def unidadmedida_view(request):
    unidadmedida = UnidadMedida.objects.all()

    return render(request, 'unidadmedida.html', {
        'unidadmedida' : unidadmedida,
        'title': 'Unidad Medida'
    })

def add_unidadmedida_view(request, unidadmedida_id=None):

    if unidadmedida_id:
        unidadmedida = UnidadMedida.objects.get(id=unidadmedida_id)
        action = 'Editar Unidad'
    else:
        unidadmedida = None
        action = 'Nueva Unidad'

    if request.method == 'POST':
        _description = request.POST['description']
        
        if unidadmedida:
            unidadmedida.description = request.POST['description']
            unidadmedida.save()
        else:
            UnidadMedida.objects.create(description=_description)

        return redirect('UnidadMedida') 
    return render(request, 'add_unidadmedida.html',{
        'unidadmedida' : unidadmedida,
        'action' : action,
    })

def delete_unidadmedida(request, id):
    unidadmedida = UnidadMedida.objects.get(pk=id)
    unidadmedida.delete()

    return redirect('UnidadMedida')

def moneda_view(request):
    moneda = Moneda.objects.all()

    return render(request, 'moneda.html', {
        'moneda' : moneda,
        'title': 'Moneda'
    })

def add_moneda_view(request, moneda_id=None):

    if moneda_id:
        moneda = Moneda.objects.get(id=moneda_id)
        action = 'Editar Moneda'
    else:
        moneda = None
        action = 'Nueva Moneda'

    if request.method == 'POST':
        _description = request.POST['description']
        
        if moneda:
            moneda.description = request.POST['description']
            moneda.save()
        else:
            Moneda.objects.create(description=_description)

        return redirect('Moneda') 
    return render(request, 'add_moneda.html',{
        'moneda' : moneda,
        'action' : action,
    })

def delete_moneda(request, id):
    moneda = Moneda.objects.get(pk=id)
    moneda.delete()

    return redirect('Moneda')