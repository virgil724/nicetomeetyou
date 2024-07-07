from django.shortcuts import render
from rest_framework import viewsets,mixins

# Create your views here.
from .serializers import NewsDetailSerializers,NewsSerializers
from .models import News


class NewsViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializers


class NewsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetailReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializers
