from django.db import models

# Create your models here.

class Type_Compatibility(models.Model):

    Type = models.CharField(max_length=10)
    Opposite = models.CharField(max_length=10)

    def __str__(self):
        return self.type, self.opposite

class Pokemon_Dictionary(models.Model):

    Type1 = models.CharField(max_length=10)
    Type2 = models.CharField(max_length=10)

    def __str__(self):
        return self.type1, self.type2