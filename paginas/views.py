from django.shortcuts import render

def home(request):
    return render(request, 'paginas/index.html')

def about(request):
    return render(request, 'paginas/about.html')

def contato(request):
    return render(request, 'paginas/contato.html')
