from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from apps.dasboard.models import Item
from api.v1.serializers import ItemSerializers
# Create your views here.

class ItemViewset(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers