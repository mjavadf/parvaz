from django.conf import settings
from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Therapist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="therapist_profile",
    )

    # Proffesional Information
    speciality = models.ManyToManyField(Speciality, related_name="therapists")
    license_number = models.CharField(max_length=100, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)

    # Contact Information
    phone_number = models.CharField(max_length=20, blank=True)
    work_email = models.EmailField(blank=True)
    office_address = models.TextField(blank=True)

    # Verification
    is_verified = models.BooleanField(default=False)
    verification_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()
