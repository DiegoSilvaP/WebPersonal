from django.shortcuts import render, HttpResponse
# HttpResponse nos permite contestar a una peticion devolviendo un codigo html en crudo
# Y render nos permite "dibujar" un template


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")