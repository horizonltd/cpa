from rest_framework import generics
from . import models
from . import serializers

class EventList(generics.ListCreateAPIView):
    queryset  = models.Event.objects.all()
    serializer_class = serializers.EvenSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Event.objects.all()
    serializer_class = serializers.EvenSerializer


#Agenda

class AgendaList(generics.ListCreateAPIView):
    queryset  = models.Agenda.objects.all()
    serializer_class = serializers.AgendaSerializer

class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Agenda.objects.all()
    serializer_class = serializers.AgendaSerializer