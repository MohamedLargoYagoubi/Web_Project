from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from web.models import Liga, Equipo, Jugador, Tabla
from django.views import generic
from .forms import *

# Create your views here.
def index(request):
    ligas = Liga.objects.all()
    dades = {
        'ligas' : ligas,
    }
    resposta = [liga.name for liga in ligas]
    return HttpResponse("<br/>".join(resposta))

def home(request):
    ligas = Liga.objects.all()
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

def createLeague(request):
    form = LigaForm()
    if request.method == "POST":
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, "web/league_form.html", context)

def updateLeague(request, pk):
    liga = Liga.objects.get(id = pk)
    form = LigaForm(instance=liga)

    if request.method == 'POST':
        form = LigaForm(request.POST, instance=liga)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, "web/league_form.html", context)

def createTeam(request):
    form = TeamForm()
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, "web/team_form.html", context)


def updateTeam(request, pk):
    equipo = Equipo.objects.get(id = pk)
    form = TeamForm(instance = equipo)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance = equipo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, "web/team_form.html", context)

def createPlayer(request):
    form = PlayerForm()
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, "web/player_form.html", context)

def updatePlayer(request, pk):
    jugador = Jugador.objects.get(id = pk)
    form = PlayerForm(instance = jugador)

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance = jugador)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, "web/player_form.html", context)