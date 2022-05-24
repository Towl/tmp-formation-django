from django.contrib.auth.models import User, Group
from myproject.myapp import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class SimpleVMSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VM
        fields = ["url", "hostname", "os"]


class PersonSerializer(serializers.ModelSerializer):
    owned_vms = serializers.HyperlinkedRelatedField(
        read_only=False,
        queryset=models.VM.objects.filter(locked=False),
        many=True,
        view_name="vm-detail",
    )

    class Meta:
        model = models.Person
        fields = ["login", "nom", "prenom", "owned_vms"]


class VMSerializer(serializers.ModelSerializer):
    owner = PersonSerializer(read_only=True)

    class Meta:
        model = models.VM
        fields = ["url", "hostname", "cpu", "ram", "os", "owner", "owner_id"]

    def to_representation(self, instance):
        result = super().to_representation(instance)
        if instance.owner is not None:
            result["owner_login"] = instance.owner.login
        return result
