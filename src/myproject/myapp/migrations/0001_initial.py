# Generated by Django 4.0.4 on 2022-05-24 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myproject.myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="MapUserVM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("access_date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("login", models.CharField(max_length=100)),
                ("nom", models.CharField(blank=True, max_length=200, null=True)),
                ("prenom", models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                "unique_together": {("nom", "prenom")},
            },
            bases=("auth.user",),
            managers=[
                ("objects", myproject.myapp.models.PersonManager()),
            ],
        ),
        migrations.CreateModel(
            name="VM",
            fields=[
                (
                    "hostname",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("cpu", models.PositiveIntegerField(default=0)),
                ("ram", models.PositiveIntegerField(default=0)),
                ("os", models.CharField(max_length=200)),
                ("locked", models.BooleanField(default=False)),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owned_vms",
                        to="myapp.person",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="vms", through="myapp.MapUserVM", to="myapp.person"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="mapuservm",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.person"
            ),
        ),
        migrations.AddField(
            model_name="mapuservm",
            name="vm",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.vm"
            ),
        ),
    ]
