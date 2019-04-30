from django.urls import path
from . import views

#This bind the views created in views.py class of the hub
urlpatterns = [
    path('', views.EventList.as_view()),
    path('<int:pk>/', views.EventDetail.as_view()), #This get the ID of the passed lecture


    path('', views.AgendaList.as_view()),
    path('<int:pk>/', views.AgendaDetail.as_view()), #This get the ID of the passed lecture
]
