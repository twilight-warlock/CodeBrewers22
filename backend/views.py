from rest_framework import viewsets
from .serializer import *
from .models import *
from django.views.generic import View
from django.shortcuts import render


class SampleView(viewsets.ModelViewSet):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
