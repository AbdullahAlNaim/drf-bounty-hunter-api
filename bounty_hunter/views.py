from rest_framework import generics
from .models import Creature
from .serializers import CreatureSerializer

# Create your views here.
class Bounty(generics.ListCreateAPIView):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer