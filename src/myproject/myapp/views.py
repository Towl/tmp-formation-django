from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myproject.myapp import serializers, models


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class VMViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VMSerializer
    queryset = models.VM.objects.all()

    def perform_update(self, serializer):
        super().perform_update(serializer)


@api_view()
def hello_world(request, who):
    return Response({"message": f"Hello, {who}!"})
