from django.shortcuts import render

# Create your views here.

def main_CxC(request):
    return render(request, 'main_CxC.html',{
        'title':'Credito y Cobranza',
    })