from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

def main_CxC(request):
    return render(request, 'main_CxC.html',{
        'title':'Credito y Cobranza',
    })

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre', 'precio']  # Campos por los que se puede filtrar
    search_fields = ['nombre']  # Búsqueda por nombre
    ordering_fields = ['precio']  # Ordenar por precio