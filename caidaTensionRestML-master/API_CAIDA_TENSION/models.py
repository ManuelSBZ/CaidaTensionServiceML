from django.db import models

# Create your models here.
class DatosCalculoCTModel(models.Model):
    """docstring forDatos_modelo. Tabla de datos que simulan las entradas al modelo"""
    id= models.AutoField(primary_key=True)
    carga=models.FloatField()
    temperatura=models.FloatField()
    ct=models.FloatField()
