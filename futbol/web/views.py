from django.shortcuts import render
from django.http import Http404, HttpResponse
from web.models import Liga, Equipo, Jugador, Tabla
from django.views import generic

# Create your views here.
def index(request):
    ligas = Liga.objects.all()[:5]
    dades = {
        'ligas' : ligas,
    }
    resposta = [liga.name for liga in ligas]
    return HttpResponse("<br/>".join(resposta))

class EquipoView(generic.DetailView):
    model = Equipo
    template_name = 'web/equipo.html'

def home(request):
    ligas = Liga.objects.all()[:5]
    return render(request, "web/index.html", {"ligas": ligas})

def liga(request, liga_id):
    try:
        liga = Liga.objects.get(pk=liga_id)
    except Liga.DoesNotExist:
        raise Http404("Esta Liga no existe")
    return render(request, "web/liga.html", {"liga": liga})