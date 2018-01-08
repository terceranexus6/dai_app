from django.shortcuts import render, HttpResponse
from .models import restaurantes

# Create your views here.

#def index(request):

def index(request):
    context = {'mensaje': 'Hola mundo!'}
    return render(request, 'base.html', context)

def test_template(request):
    context = {} #variables de plantilla
    return render(request, 'test.html',context)

def test_template(request):
    iterador = restaurantes.find().limit(10)
    context = {
        "lista": list(iterador)
    }
    return render(request, 'test.html',context)

def nuevo_restaurante(request):

   form = RestauranteForm()
   if request.method == 'POST':
      form = RestauranteForm(request.POST)
      if form.is_valid():                   # se pasan los validadores
         datos = form.cleaned_data
         #...
         return redirect('/donde_sea')

   # GET o error de validación
   context = {
      'form': form,              # en blanco o rellena con errores
   }
   return (request, 'form.html', context)
