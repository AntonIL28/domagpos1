from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class AddProducto(forms.Form):
    codigo = forms.CharField(
        label = "Codigo"
    )
    description = forms.CharField(
        label = "Descripcion"
    )
    Unidad_Compras = forms. IntegerField(
        label= "Unidad Compras"
    )
    Unidad_Ventas = forms. IntegerField(
        label= "Unidad Ventas"
    )
    Unidad_Inv = forms. IntegerField(
        label= "Unidad Inventario"
    )
    cantidad_Unidad_Compras= forms. IntegerField(
        label="Cantidad Compras"
    )
    Cto_Unidad_Compras = forms. FloatField(
        label="Costo Unitario"
    )
    Cto_Factura = forms. FloatField(
        label="Costo Factura"
    )
    Porc_GastosVarios = forms. CharField(
        label="Porcentaje de Gastos Varios"
    )
    Porc_impuestos = forms. CharField(
        label="Porcentaje Impuesto"
    )
    Cto_Integrado = forms. FloatField(
        label="Costo Integrado"
    )
    
