from rest_framework import serializers# Objeto para establecer los tipos de datos permitidos en el serializador
from rest_framework.serializers import Serializer, ModelSerializer
from API_CAIDA_TENSION.models import DatosCalculoCTModel


class DatosCalculoCTSerializer(ModelSerializer):
    """docstring forDatos_modelo. Tabla de datos que simulan las entradas al modelo"""
    class Meta:
        model=DatosCalculoCTModel
        fields="__all__"
    id= serializers.IntegerField()
    carga=serializers.FloatField()
    temperatura=serializers.FloatField()
    ct=serializers.FloatField()

class DatosCalculoCTSerializerpost(ModelSerializer):
    class Meta:
        model=DatosCalculoCTModel
        fields=("carga","temperatura","ct")
    carga=serializers.FloatField()
    temperatura=serializers.FloatField()
    ct=serializers.FloatField()

