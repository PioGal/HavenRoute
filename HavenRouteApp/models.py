from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Amenity(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Port(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='')
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    amenities = models.ManyToManyField(Amenity, blank=True)

class Route(models.Model):
    name = models.CharField(max_length=128, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stop_list = models.ManyToManyField(Port, through='RoutePort')

class RoutePort(models.Model):
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()


class Cruise(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    attendees = models.ManyToManyField(User, related_name='trip_attendees')
    created_by = models.ManyToManyField(User, related_name='creator')



