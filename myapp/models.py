from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\+?\d{11}$',
        message="Phone number must be entered in the format: '+923111234567'. 11 digits required."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)  # validators should be a list
    postal_code = models.CharField(max_length=200, default="e.g 38000")
    province = models.CharField(max_length=200, default="e.g Punjab")
    education = models.CharField(max_length=400, default = "Your Academical status")
    address = models.CharField(max_length=2000, default="Your address")
    country = models.CharField(max_length=200, default="Pakistan")
    gender = models.CharField(max_length=200, default="Male/Female")
    designation = models.CharField(max_length=200, default="Therapist/Rehabilitationist")
    cnic = models.CharField(max_length=200, default="33100-7947702-1")
    experience = models.CharField(max_length = 2000, default="")
    additional_details = models.CharField(max_length = 5000, default="")
    
    def __str__(self):
        return f'profile of user "{self.user.username}"'
    
    
    
class Patient(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, default="")
    cnic = models.CharField(max_length=200)
    age = models.CharField(max_length=200, default ="")
    phone_number = models.CharField(max_length=200)
    drug_addiction = models.CharField(max_length=200)
    plan = models.CharField(max_length=200)
    fees = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Center(models.Model):
    Profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')  
    orgranization_name = models.CharField(max_length=200)
    mode_of_organization = models.CharField(max_length=200)
    description = RichTextField()

    def __str__(self):
        return self.organization_name

    