from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"api/sample", SampleView)

urlpatterns = [path("", Index.as_view(), name="index")] + router.urls
