from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import User


# @admin.register(User)
# class UserAdmin(admin.OSMGeoAdmin):
#     # list_display = ("username", "location")
#     pass

class UserAdmin(LeafletGeoAdmin):
    model = User

admin.site.register(User, UserAdmin)