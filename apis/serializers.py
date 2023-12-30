# import serializer from rest framework
from rest_framework import serializers

# import model from models.py
from .models import RestModel

# Create a model serializer
class  RestSerializer(serializers.HyperlinkedModelSerializer):
    # Specify model and fields
    class Meta:
        model = RestModel
        fields = ('title', 'description')