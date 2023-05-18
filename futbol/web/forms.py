from django.forms import ModelForm
from .models import *

class LigaForm(ModelForm):
    class Meta:
        model = Liga
        fields = '__all__'

class TeamForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class PlayerForm(ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
    