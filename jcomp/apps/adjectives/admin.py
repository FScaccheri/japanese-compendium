from django.contrib import admin
from .models import Adjective


class AdjectiveAdmin(admin.ModelAdmin):
    pass


admin.site.register(Adjective, AdjectiveAdmin)
