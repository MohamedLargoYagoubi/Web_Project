"""futbol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import web.views as wv

urlpatterns = [
    path("", wv.home, name="home"),
    path("liga/<int:liga_id>/", wv.liga, name = 'Liga'),
    path("equipo/<int:equipo_id>/", wv.equipo, name = 'Equipo'),
    path("jugador/<int:jugador_id>/", wv.jugador, name = 'Jugador'),
    path("admin/", admin.site.urls),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
    path("", wv.nav_bar, name="nav_bar"),
    path("create_league/", wv.createLeague, name="create_league"),
    path("create_team/", wv.createTeam, name="create_team"),
    path("create_player/", wv.createPlayer, name="create_player"),
    path("update_league/<str:pk>/", wv.updateLeague, name="update_league"),
    path("update_team/<str:pk>/", wv.updateTeam, name="update_team"),
    path("update_player/<str:pk>/", wv.updatePlayer, name="update_player"),

]
