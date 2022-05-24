from rest_framework import viewsets
from myproject.myapp import serializers, models


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class VMViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VMSerializer
    queryset = models.VM.objects.all()

    def perform_update(self, serializer):
        super().perform_update(serializer)
