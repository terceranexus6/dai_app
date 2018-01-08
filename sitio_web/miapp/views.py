from django.shortcuts import render
from django.http import HttpResponse
from .models import hamlet
from miapp.forms import PersonajeForm

def index(request):
    context = {
        'tittle' : "HAMLET",
        'frase' : "Alas, he's mad!",
        'linkgithub' : "https://www.github.com/terceranexus6"
    }
    return render(request, 'test.html', context)

#def test_t(request):
#    iterador = hamlet.find().limit(2)
#    context = {
#        "lista" : list(iterador)
#    }
#    return render(request, "prueba.html", context)

def nuevo_personaje(request):

   form = PersonajeForm()
   if request.method == 'POST':
      form = PersonajeForm(request.POST)
      #if form.is_valid():                   # se pasan los validadores
        # datos = form.cleaned_data
         #...
         #return redirect('/donde_sea')

   # GET o error de validación
   context = {
      'form': form,              # en blanco o rellena con errores
   }
   return render(request, 'form.html', context)
