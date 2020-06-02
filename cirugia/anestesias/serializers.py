from rest_framework import serializers
from anestesias.models import Anestesia


class AnestesiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anestesia
        fields = '__all__'
