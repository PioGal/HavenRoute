from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout


from HavenRouteApp.models import Amenity, Port, Route, RoutePort, Cruise
from HavenRouteApp.forms import *



class PortListView(ListView):
    model = Port
    template_name = 'Port_List.html'

class AmenitiesListView(ListView):
    model = Amenity
    template_name = 'Amenity_List.html'

class CruiseView(ListView):
    model = Cruise
    template_name = 'Cruise_View.html'

class AddPortsView(View):

    def get(self, request):
        form = AddPortForm()
        return render(request, 'add_object.html', {'form': form})

    def post(self, request):
        form = AddPortForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Add_Port'))
        return render(request, 'add_object.html', {'form': form})

class AddAmenityView(View):

    def get(self, request):
        form = AddAmenityForm()
        return render(request, 'add_object.html', {'form': form})

    def post(self, request):
        form = AddAmenityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Add_Amenity'))
        return render(request, 'add_object.html', {'form': form})

class CreateRouteView(View):

    def get(self, request):
        form = CreateRouteForm()
        return render(request, 'create_route.html', {'form':form})

    def post(self,request):
        form = CreateRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Create_Route'))
        return render(request, 'create_route.html', {'form': form})



