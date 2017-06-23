from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re

# Create your models here.

def validateword(value):
    if len(value) < 2:
        raise ValidationError('Field must be greater than 2')
    pattern = re.compile("[A-Za-z]+$")
    if re.match(pattern, value) == None:
        raise ValidationError('Only letters please.')

class User(models.Model):
    first_name = models.CharField(max_length=100, validators=[validateword])
    last_name = models.CharField(max_length=100, validators=[validateword])
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
