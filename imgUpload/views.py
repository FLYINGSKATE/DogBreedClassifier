# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ImageUploadForm
from keras.applications.resnet import ResNet50
import keras.utils as image
from keras.applications.resnet import preprocess_input,decode_predictions
import numpy as np
# Create your views here.

def handle_uploaded_file(f):
    with open('img.jpg','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk);

def imageUpload(request):
    return render(request,'uploadImage.html')

def home(request):
    return render(request,'uploadImage.html')

def imageprocess(request):
    res=[]
    form = ImageUploadForm(request.POST,request.FILES)
    handle_uploaded_file(request.FILES['image'])
    model = ResNet50(weights='imagenet')
    img_path = 'img.jpg'
    img = image.image_utils.load_img(img_path,target_size=(224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    print('Predicted:',decode_predictions(preds,top=3)[0])
    html = decode_predictions(preds,top=3)[0]
        
    for e in html:
        res.append((e[1],np.round(e[2]*100,2)))
        
        
    return render(request,'result.html',{'res':res})        
