from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    introduction = models.CharField(blank=True, max_length=100)
    theme = models.TextField(max_length=255, default='Theme of Event')
    created_on = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(default='')
    location = models.CharField(max_length=100, blank=True, default='')


    def __str__(self):
        return self.title


class Agenda(models.Model):
    documentary_on_cpn = models.CharField(max_length=255)
    agenda_title = models.ForeignKey(Event, related_name='agendas', on_delete=models.CASCADE)
    arrival_and_registraion = models.CharField(max_length=255)
    induction_programme = models.IntegerField()
    welcome_address = models.CharField(max_length=255)
    induction_lectures = models.CharField(max_length=255)
    induction_of_new_members = models.CharField(max_length=255)
    welcome_address_by_president = models.CharField(max_length=150)
    remarks = models.CharField(max_length=200)
    photograph = models.CharField(max_length=255)
    documentary_on_cpn = models.CharField(max_length=255)
    lunch = models.CharField(max_length=255)
    annual_general_meeting = models.CharField(max_length=255)
    dinner_and_presentation_of_awards_and_certificate = models.CharField(
        max_length=255)

    def __str__(self):
        return self.documentary_on_cpn
