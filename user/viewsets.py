from xmlrpc.client import ResponseError
from rest_framework import viewsets
from rest_framework_gis import filters
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    """User view set."""
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permisson_classes = []

    def list(self, request, id=None):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

