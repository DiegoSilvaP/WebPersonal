from django.shortcuts import render
# Podemos usar el "Project" desde los modelos de la app portfolio
from .models import Project
# Create your views here.


def portfolio(request):
    # Vamos a crear una lista de proyectos, hacemos referencia a la clase Project, donde tenemos nuestros proyectos
    # y llamamos a .objects, que gestiona en tiempo de ejecución cada modelo mediante el método .all
    projects = Project.objects.all()
    # Ahora hay que inyectar la lista de proyectos en el template
    # Se pasa como un diccionario de contexto 
    return render(request, "portfolio/portfolio.html", {'projects':projects})
    # Un QuerySet es la representanción de una consulta a la base de datos pero devuelta como una lista de instancias del tipo que ha encontrado