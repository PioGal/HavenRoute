
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView


from django.contrib.auth import authenticate, login, logout


from HavenRouteApp.models import Amenity, Port, Route, RoutePort, Cruise
from HavenRouteApp.forms import AddPortForm, AddAmenityForm, CreateRouteForm, AddPortRouteForm



class PortListView(ListView):
    model = Port
    template_name = 'Port_List.html'

class AmenitiesListView(ListView):
    model = Amenity
    template_name = 'Amenity_List.html'

class CruiseView(ListView):
    model = Cruise
    template_name = 'Cruise_View.html'

class RouteView(ListView):
    model = Route
    template_name = 'RouteView.html'

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

class PortDetailView(DetailView):
    model = Port
    template_name = 'porty/port_detail_view.html'

class PortUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['filmy.change_film']

    model = Port
    template_name = 'add_object.html'
    fields = '__all__'

    def get_success_url(self):
        super().get_success_url()
        return reverse("update_port", args=(self.object.id,))


class PortUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['port.change_film']

    model = Port
    template_name = 'add_object.html'
    fields = '__all__'


    def get_success_url(self):
        super().get_success_url()
        return reverse("update_port", args=(self.object.id,))

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
        return render(request, 'create_route.html',{'form': form})

    def post(self,request):
        form = CreateRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Create_Route'))
        return render(request, 'create_route.html', {'form': form})

class RouteDetailView(DetailView):
    model = Route
    template_name = 'porty/route_detail_view.html'

class AddPortRouteView(CreateView):
    model = RoutePort
    template_name = 'add_object.html'
    fields = '__all__'
    success_url = reverse_lazy('add_port_route')

class AddCruiseView(CreateView):
    model = Cruise
    template_name = 'add_object.html'
    fields = '__all__'
    success_url = reverse_lazy('add_cruise')

class CruiseDetailView(DetailView):
    model = Cruise
    template_name = 'porty/cruise_detail_view.html'


