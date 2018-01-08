from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'boldmessage' : "I'm a bold message"}
    return render(request, 'test/index.html', context)
