from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.category, name="category"),
    path('productbycat/<int:pk>',views.productbycat,name="productbycat"),
]
