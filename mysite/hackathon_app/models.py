from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    pass
    # types = MultiSelectField(choices=TYPE_CHOICES, max_length=50, max_choices=3)
    # phone = PhoneNumberField(null=True, blank=True, region='KG')
