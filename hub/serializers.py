from rest_framework import serializers
#from hub.models import Lecture
from .import models

class EvenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Event
        fields = '__all__'
class AgendaSerializer(serializers.ModelSerializer):


    class Meta:
        
        model  = models.Agenda
        fields = '__all__'