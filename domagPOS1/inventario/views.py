from django.shortcuts import render,redirect
from inventario.models import Category,Product
from django.contrib import messages

# Create your views here.
def category(request):
    category = Category.objects.all()
    return render(request,'category.html',{
        'category' : category,
        'title' : 'Categorias'})

def productbycat(request,pk):
    if pk == 0:
        category = ""
    else:
        category = Category.objects.get(id=pk)
    try:
        if pk == 0:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(categories=pk)
        return render(request,'productbycat.html',{'category' : category,'products': products,'title' : 'Listado de productos'})
    except:
        messages.success(request,("ERROR Desconocido"))
        return redirect('inventario_main')

#Vistas Main para los productos
def lista_abrasive(request):

    products = Product.objects.all()

    return render(request, 'abrasive/lista_abrasive.html',{
        'title':'Abrasivos',
        'products' : products
    })