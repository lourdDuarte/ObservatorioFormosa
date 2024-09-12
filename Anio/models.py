from django.db import models

# Create your models here.

class Año(models.Model):
    año = models.CharField(max_length=200, blank=False, null=False)

    def __str__ (self):
        return self.año