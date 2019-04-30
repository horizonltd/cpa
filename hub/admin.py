from django.contrib import admin
from . models import Event, Agenda
# Register your models here.


class EventAdmin(admin.ModelAdmin):

    search_fields = ['id','title']
class AgendaAdmin(admin.ModelAdmin):

    search_fields = ['__all__']



admin.site.register(Event, EventAdmin)
admin.site.register(Agenda, AgendaAdmin)