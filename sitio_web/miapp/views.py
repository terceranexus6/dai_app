from django.shortcuts import render
from django.http import HttpResponse
from .models import hamlet

def index(request):
    context = {
        'tittle' : "HAMLET",
        'frase' : "Alas, he's mad!",
        'linkgithub' : "https://www.github.com/terceranexus6"
    }
    return render(request, 'test.html', context)

def test_t(request):
    iterador = hamlet.find().limit(2)
    context = {
        "lista" : list(iterador)
    }
    return render(request, "prueba.html", context)
