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








class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128,
                               widget=forms.PasswordInput)


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Hasła się nie zgadzają!')
        return data