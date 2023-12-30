# import viewsets

from rest_framework import viewsets

# import local data
from .serializers import RestSerializer
from .models import RestModel

# create a viewset

class RestViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = RestModel.objects.all()

    # specify serializer to be used
    serializer_class = RestSerializer