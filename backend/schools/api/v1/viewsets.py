from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from schools.api.v1.serializers import SchoolSerializer
from schools.models import School


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    permission_classes = [AllowAny]
