from anestesias.models import Anestesia
from anestesias.serializers import AnestesiaSerializer
from rest_framework import viewsets, permissions

class AnestesiaViewSet(viewsets.ModelViewSet):
    queryset = Anestesia.objects.all()
    serializer_class = AnestesiaSerializer
    
    permission_classes = [
        permissions.AllowAny
        ]

