from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'tittle' : "HAMLET",
        'frase' : "Alas, he's mad!",
        'linkgithub' : "https://www.github.com/terceranexus6"
    }
    return render(request, 'test.html', context)
