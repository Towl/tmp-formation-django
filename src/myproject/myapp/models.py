from django.db import models


class Person(models.Model):
    login = models.CharField(max_length=100)
    nom = models.CharField(max_length=200, blank=True, null=True)
    prenom = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = [["nom", "prenom"]]

    def __str__(self):
        return f"{self.login}"


class MapUserVM(models.Model):
    vm = models.ForeignKey("VM", on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    access_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vm} / {self.person}"


class VM(models.Model):
    hostname = models.CharField(max_length=200, primary_key=True)
    cpu = models.PositiveIntegerField(default=0)
    ram = models.PositiveIntegerField(default=0)
    os = models.CharField(max_length=200)
    owner = models.ForeignKey(
        Person, on_delete=models.CASCADE, null=True, related_name="owned_vms"
    )
    users = models.ManyToManyField(
        Person, related_name="vms", through="MapUserVM", through_fields=("vm", "person")
    )

    def __str__(self):
        return f"{self.hostname}"
