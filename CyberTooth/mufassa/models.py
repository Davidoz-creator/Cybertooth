from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=50,
    )
    description=models.TextField(
        null=False,
        blank=False,
        max_length=200,
    )
    slug=models.SlugField( )

 
def __str__(self):
       return self.name
 

class skytouch(models.Model):
    name=models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=50
    )
description=models.TextField(
    null=False,
    blank=False,
    max_length=2000,
)

destinations=models.ManyToManyField(
    Destination,
    related_name='destinations'
)