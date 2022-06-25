from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from SerializerRelationsApi.models import Singer, Song
from SerializerRelationsApi.serializer import SingerSerializer, SongSerializer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongsViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
