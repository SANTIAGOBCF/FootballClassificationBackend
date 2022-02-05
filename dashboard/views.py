from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import tensorflow as tf
from tensorflow import keras
import json,os
# Create your views here.

def result(request):
    #Abrir NN guardada
    #x=[[1.0]*33]
    x=[[2.532391,1.018293,2.13019,2.434969,2.20101,2.491028,2.925359,2.236808,2.255005,1.767403,
        1.451998,1.861977,3.68012,2.195558,1.713647,0.246064,0.552243,-0.50339,2.434084,-0.453532,
        -1.193549,2.254888,2.869478,1.684657,3.265669,-0.717896,-0.90947,-0.92385,-0.599889,-0.318983,
        -0.074713,-0.140266,-0.485159]]
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'static/model.json')
    json_file=open(file_path,"r")
    model_json=json_file.read()
    json_file.close()
    modelo_cargado=tf.keras.models.model_from_json(model_json)
    modelo_cargado.load_weights(os.path.join(module_dir, 'static/model.h5'))
    print("Se cargo el modelo!!")
    res=np.around(modelo_cargado.predict(x), decimals=4)
    return HttpResponse(res)

"""def pro(request):
    response = HttpResponse(request.headers)
    
    return response"""