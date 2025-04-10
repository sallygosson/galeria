from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Bem-vindo à Homepage!</h1>")

def about(request):
    return HttpResponse("<h1>Sobre nós</h1><p>Esta é a página About.</p>")
