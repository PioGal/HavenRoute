from django import forms
from HavenRouteApp.models import Amenity, Port, Route, RoutePort, Cruise
from django.contrib.auth.models import User



class AddPortForm(forms.ModelForm):

    class Meta:
        model = Port
        fields = '__all__'
        widgets = {
            'amenities': forms.CheckboxSelectMultiple
        }

class AddAmenityForm(forms.ModelForm):

    class Meta:
        model = Amenity
        fields = '__all__'

class CreateRouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = '__all__'

    name = forms.CharField()
    date = forms.DateInput

    routeport = forms.ModelMultipleChoiceField(
        queryset=RoutePort.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
