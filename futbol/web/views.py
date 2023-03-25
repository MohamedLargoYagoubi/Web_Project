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

def home(request):
    ligas = Liga.objects.all()[:5]
    return render(request, "web/index.html", {"ligas": ligas})

def liga(request, liga_id):
    try:
        liga = Liga.objects.get(pk=liga_id)
        equipos = Equipo.objects.filter(liga__pk=liga_id)
    except Liga.DoesNotExist:
        raise Http404("Esta Liga no existe")
    return render(request, "web/liga.html", {"liga": liga, "equipos":equipos})

def equipo(request, equipo_id):
    try:
        equipo = Equipo.objects.get(pk=equipo_id)
        jugadores = Jugador.objects.filter(equipo__pk=equipo_id)
    except Equipo.DoesNotExist:
        raise Http404("Este Equipo no existe")
    return render(request, "web/equipo.html", {"equipo": equipo, "jugadores":jugadores})

def jugador(request, jugador_id):
    try:
        jugador = Jugador.objects.get(pk=jugador_id)
    except Equipo.DoesNotExist:
        raise Http404("Este Jugador no existe")
    return render(request, "web/jugador.html", {"jugador": jugador})

def nav_bar(request):
    return render(request, "web/nav_bar.html", {})