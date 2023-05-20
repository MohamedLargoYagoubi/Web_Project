from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.http import HttpRequest
from .models import *
from .views import *

class AddModifyDeleteTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_League(self):
        form_data = {'name': 'Test League'}
        request = self.factory.post("create_league", data=form_data)
        
        # Call the view function
        response = createLeague(request)

        # Assert that a new Liga object was created
        self.assertEqual(Liga.objects.count(), 1)
        liga = Liga.objects.first()
        self.assertEqual(liga.name, 'Test League')

        form_data = {"name": "Test League 2"}
        request = self.factory.post("update_league", data=form_data)

        response = updateLeague(request, 1)

        self.assertEqual(Liga.objects.count(), 1)
        liga = Liga.objects.first()
        self.assertEqual(liga.name, 'Test League 2')

        request = self.factory.post("delete_league", data=form_data)

        response = deleteLeague(request, 1)

        self.assertEqual(Liga.objects.count(), 0)

    def test_Team(self):
        liga = Liga.objects.create(name="Test League")
        liga.save()
        form_data = {'name': 'Test Team', 'liga': 1}
        request = self.factory.post("create_team", data=form_data)
        
        response = createTeam(request)

        self.assertEqual(Equipo.objects.count(), 1)
        equipo = Equipo.objects.first()
        self.assertEqual(equipo.name, 'Test Team')

        form_data = {"name": "Test Team 2", "liga": 1}
        request = self.factory.post("update_team", data=form_data)

        response = updateTeam(request, 1)

        self.assertEqual(Equipo.objects.count(), 1)
        equipo = Equipo.objects.first()
        self.assertEqual(equipo.name, 'Test Team 2')

        request = self.factory.post("delete_team", data=form_data)

        response = deleteTeam(request, 1)

        self.assertEqual(Equipo.objects.count(), 0)

    def test_Player(self):
        liga = Liga.objects.create(name="Test League")
        liga.save()
        equipo = Equipo.objects.create(name = "Test Team", liga = liga)
        equipo.save()
        form_data = {'name': 'Test Player', "equipo": 1, "edad": 18, "posicion": "Delantero", "años_exp": 0}
        request = self.factory.post("create_player", data=form_data)
        
        response = createPlayer(request)

        self.assertEqual(Jugador.objects.count(), 1)
        jugador = Jugador.objects.first()
        self.assertEqual(jugador.name, 'Test Player')

        form_data = {'name': 'Test Player 2', "equipo": 1, "edad": 18, "posicion": "Delantero", "años_exp": 0}
        request = self.factory.post("update_player", data=form_data)

        response = updatePlayer(request, 1)

        self.assertEqual(Jugador.objects.count(), 1)
        jugador = Jugador.objects.first()
        self.assertEqual(jugador.name, 'Test Player 2')

        response = deleteLeague(request, 1)

        self.assertEqual(Jugador.objects.count(), 0)

    
