from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.


class SampleView(viewsets.ModelViewSet):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()
