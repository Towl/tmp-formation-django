import logging
from django.contrib import admin
from myproject.myapp import models

logger = logging.getLogger(__name__)


@admin.register(models.VM)
class VMAdmin(admin.ModelAdmin):
    list_display = ("hostname", "os", "cpu", "ram", "owner", "display_users")

    @admin.display(description="Users")
    def display_users(self, obj):
        value = ""
        for person in obj.users.all():
            value += f"{person}\n"
        return value


@admin.register(models.MapUserVM)
class MapUserVMAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        logger.info(request.user)
        return False


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass
