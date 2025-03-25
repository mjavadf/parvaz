from django.contrib import admin

from .models import Speciality
from .models import Therapist


@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    pass


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass
