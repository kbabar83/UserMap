from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget

from .models import User

class UpdateUserForm(forms.ModelForm):
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    class Meta:
        model = User
        fields = ('username','email','address','location','phone_number')
        widgets = {'location': LeafletWidget()}