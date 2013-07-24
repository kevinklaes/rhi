from django.db import models

class Survey(models.Model):
    # Page 1
    age = models.IntegerField(max_length=3)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=9)
    sexual_orientation = models.CharField(max_length=40)
    gender_identity = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    ethnicity = models.CharField(max_length=40)
