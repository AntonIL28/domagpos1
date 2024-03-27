from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Productos

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

class AddCliente(forms.Form):
    razon = forms.CharField(
        label = "Razon"
    )
    rfc = forms.CharField(
        label = "RFC"
    )

    credit_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    credito = forms.TypedChoiceField(
        label = "Credito",
        choices = credit_options
    )
    limite_credito = forms.IntegerField(
        label= "Limite de Credito"
    )
    dias_credito = forms.IntegerField(
        label= "Dias de credito"
    )
    lista_precios = forms. IntegerField(
        label= "Lista de precios"
    )
    nombre_comercial = forms.CharField(
        label= "Nombre Comercial"
    )
    dirEstado = forms.CharField(
        label="Estado"
    )
    dirCiudad= forms.CharField(
        label="Ciudad"
    )
    dirColonia = forms.CharField(
        label = "Colonia"
    )
    dircalle = forms.CharField(
        label = "Calle"
    )
    dirnumext = forms. IntegerField(
        label= "Numero Exterior"
    )
    dirnumint = forms. IntegerField(
        label= "Numero Interior"
    )
    telefono= forms.CharField(
        label= "Telefono"
    )

class AddProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['description',
                  'codigo',
                'Unidad_Compras',
                'Unidad_Ventas',
                'Unidad_Inv',
                'cantidad_Unidad_Compras',
                'Cto_Unidad_Compras',
                'Porc_GastosVarios',
                'Porc_impuestos']
        
        labels={
                'codigo':'Codigo',
                'description':'Descripcion',
                'Unidad_Compras':'Unidad Compra',
                'Unidad_Ventas': 'Unidad Venta',
                'Unidad_Inv':'Inventario',
                'cantidad_Unidad_Compras':'Unidades',
                'Cto_Unidad_Compras':'Costo Unitario',
                'Porc_GastosVarios':'Porc. Gastos Varios',
                'Porc_impuestos':'Porc. Impuesto'
        }
