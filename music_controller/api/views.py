from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

last_five_days = patient_vales.objects.filter(pub_date__gte=datetime.now()-timedelta(days=5))