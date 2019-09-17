from django.urls import include, path
from .models import Arduino

from .serializers import ArduinoSerializer

from rest_framework.generics import CreateAPIView

app_name = 'api'

urlpatterns = [
    path('create', CreateAPIView.as_view(serializer_class = ArduinoSerializer)),                                    # get: list over order le is making. post
   
            ]