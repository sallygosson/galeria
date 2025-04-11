from django.shortcuts import render

def home(request):
    return render(request, 'paginas/index.html')

def sobre(request):
    return render(request, 'paginas/sobre.html')

def contato(request):
    return render(request, 'paginas/contato.html')
