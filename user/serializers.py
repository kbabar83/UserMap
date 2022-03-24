
from rest_framework_gis import serializers

from .models import User


class UserSerializer(serializers.GeoFeatureModelSerializer):
    """User GeoJSON serializer."""

    class Meta:
        """User serializer meta class."""

        fields = ("id", "username")
        geo_field = "location"
        model = User
