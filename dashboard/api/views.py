from dashboard.models import Features
from dashboard.api.serializers.general_serializer import FeaturesSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from dashboard.api.serializers.general_serializer import FeaturesPositionSerializer
import numpy as np
import tensorflow as tf
from tensorflow import keras
import json,os
from pathlib import Path
from dashboard.api.utils import generateResult,dictToList

class FeaturesViewSet(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesPositionSerializer
    http_method_names = ['get', 'post', 'delete']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return FeaturesSerializer
        if self.action == 'delete':
            return FeaturesSerializer
        if self.action == 'retrieve':
            return FeaturesSerializer
        else:
            return FeaturesPositionSerializer
    
    def create(self, request):
        serializer = FeaturesPositionSerializer(data = request.data)        
        if serializer.is_valid():
            x=[dictToList(serializer._validated_data.values())]
            feature=serializer.save()           
            module_dir = Path(__file__).resolve().parent.parent
            file_path = os.path.join(module_dir, 'static/model.json')
            json_file=open(file_path,"r")
            model_json=json_file.read()
            json_file.close()
            modelo_cargado=tf.keras.models.model_from_json(model_json)
            modelo_cargado.load_weights(os.path.join(module_dir, 'static/model.h5'))
            print("Se cargo el modelo!!")
            res=np.around(modelo_cargado.predict(x), decimals=2)
            indices=np.argsort(res[0])            
            answer=generateResult(res[0], indices)
            feature.position=answer[3]
            feature.save()
            return Response({'message':'Features created correctly',"position": answer },status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    