from rest_framework.serializers import ModelSerializer
from apps.dasboard.models import *

class ItemSerializers(ModelSerializer):
    class Meta :
        model = Item
        fields = ['name','description']