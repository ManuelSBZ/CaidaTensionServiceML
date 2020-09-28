from django.shortcuts import render
# Create your views here.
from .models import DatosCalculoCTModel
from .serializer import DatosCalculoCTSerializer, DatosCalculoCTSerializerpost
from rest_framework.views import APIView,Response
from rest_framework.exceptions import NotFound
from rest_framework import generics, mixins
from .modelo_ML_CT.CT import Ct #importando CLASE del modelo creado en el script del modulo
#from sklearn.externals import joblib


# Create your views here.

# class VideoJuegosView(viewsets.ModelViewSet):
#   queryset=VideoJuegosModel.objects.all()
#   serializer_class= VideoJuegosSerializer



class TensionList(generics.ListAPIView):
  """docstring for CaidaTensionView"""
  serializer_class=DatosCalculoCTSerializer

  def get_queryset(self):
      object_model=DatosCalculoCTModel.objects.all()
      return object_model

  def post(self, request):
    #serializer=VideoJuegosSerializer(data=request.data)
    data= {k:v for k,v in request.data.items()}
    model=Ct()
    print("before error")
    data["ct"]= model.predict(float(data.get("carga")), float(data.get("temperatura")))
    print(data)
    serializer=DatosCalculoCTSerializerpost(data=data)
    print(serializer.is_valid())
    if serializer.is_valid():
      print("SERIALIZR IS VALID")
      valid_data=serializer.data
      #instance_register_model=VideoJuegosModel.objects.create(**valid_data)
      
      instance_register_model=DatosCalculoCTModel.objects.create(**valid_data)
      print("SERIALIZER")
          # nombre=valid_data.get("nombre")
          # genero=valid_data.get("genero")
          # anio=valid_data.get("anio")
      return(Response({"registro_id":f"{instance_register_model.id}","ct%":f"{data['ct']}"}))
    else:
      return(Response(serializer.errors))

class TensionDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = DatosCalculoCTModel.objects.all()
    serializer_class = DatosCalculoCTSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
