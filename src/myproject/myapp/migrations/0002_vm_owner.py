# Generated by Django 4.0.4 on 2022-05-12 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vm",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.person",
            ),
        ),
    ]