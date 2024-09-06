from django.db import models

# Create your models here.

class ComparacionTemporal(models.Model):
    tipo_comparacion = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.tipo_comparacion