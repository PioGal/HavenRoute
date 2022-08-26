"""HavenRoute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from HavenRouteApp import views
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('ports/', views.PortListView.as_view(), name='Port_List'),
    path('add_port/', views.AddPortsView.as_view(), name='Add_Port'),
    path('add_amenity/', views.AddAmenityView.as_view(), name='Add_Amenity'),
    path('amenities/', views.AmenitiesListView.as_view(), name='Amenities'),
    path('cruise/', views.CruiseView.as_view(), name='Cruise'),
    path('create_route/', views.CreateRouteView.as_view(), name='Create_Route'),
    path('accounts/', include('accounts.urls'))

]
