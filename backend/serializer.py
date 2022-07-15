from rest_framework import serializers
from .models import *


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ["id", "name", "detail"]
