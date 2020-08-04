from django.db import models


# Create your models here.


class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=False)
