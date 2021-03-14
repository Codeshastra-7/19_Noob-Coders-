from django.shortcuts import render
from app.models import *
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response 
from django.contrib import messages
from geopy.distance import geodesic
from app.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,reverse,redirect
from app.serializers import *
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2
from PIL import Image


location = str(os.getcwd())+'\models\eresnet152V2_model.h5'



model = load_model(location)

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def dashboard(request, id):
    user = Aadhar.objects.get(id=id)
    driver = Driver.objects.filter(contact = user)
    details = WareHouse.objects.filter(farmer = user)[0]
    context = {
        'apikey': 'AIzaSyCYUeS2YnGYNzt9kZRc1p-4tt4IyEacsjY',
        'auser': user,
        'driver': driver,
        'details': details,
    }
    return render(request,'app/dashboard.html',context)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def location(request,id,*args,**kwargs):
    drivers = Driver.objects.filter(contact__id = id)
    context = []
    for d in drivers:
        li ={}
        dest_lat = d.deliver.latitude
        dest_long = d.deliver.longitude
        dest = (dest_lat, dest_long)
        origin = (d.latitude, d.longitude)
        distance = round(geodesic(origin, dest).kilometers, 2)
        li.update({"truckno": d.truckno, "distance": distance,
                'driver_name': d.name,
                'delivery_location': d.deliver.name,
                'phonenumber': d.phonenumber,
                'urld': reverse('driverdata',args=[d.contact.id,d.id])
        })
        context.append(li)        
    return Response({"message":"success", "data": context})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def driverloc(request,id,did,*args,**kwargs):
    driver = Driver.objects.get(id=did)
    serializer = DriveLocUpdate(driver,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def datadrive(request,id,did):
    context = {
        'driver': Driver.objects.get(id=did),
        'apikey': 'AIzaSyCYUeS2YnGYNzt9kZRc1p-4tt4IyEacsjY',
    }
    return render(request,'app/datadrive.html',context )

    
def WareUpdate(request, id):
    e = WareHouse.objects.filter(farmer__id=id)[0]
        
    if request.method == "POST":
        form = WareForm(request.POST,instance=e)
        if form.is_valid():
            ware = form.save(commit=False)
            ware.farmer = Aadhar.objects.get(id=id)
            ware.save()
            messages.success(request,'Successfully updated!')
            return HttpResponseRedirect(reverse('dashboard',args=[id]))
    
    context = {
        'form' : WareForm(instance=e)   
    }   
    return render(request,'app/wareup.html',context)


def qrgenerate(request, id):
    user = Aadhar.objects.filter(id=id)[0]
    data = TransportItems.objects.filter(farmer__id = id).order_by('-id')
    context = {
        'data': data, 
        'auser': user, 
    }
    if request.method == "POST":
        form = ItemsUpdate(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            item = form.save(commit=False)
            print('reached')
            item.farmer = Aadhar.objects.filter(id = id)[0]
            item.drive = Driver.objects.filter(contact__id= id)[0]
            item.save()
            messages.success(request,'Added successfully')
            return render(request, 'app/qrgen.html',context)
        return render(request, 'app/qrgen.html',context)        
    return render(request, 'app/qrgen.html',context)


def qrdata(request,id, qid):
    data = TransportItems.objects.get(id = qid)

    context ={
        'data': data,
    }
    return render(request,'app/qrdata.html',context)

def scan(request):
    return render(request, 'app/scan.html')

def help(request):
    return render(request,'app/help.html')

def marketplace(request):
    context = {
        'items': Marketplace.objects.all(),
    }
    return render(request, 'app/marketplace.html',context)

def model_predict(img, model):
    loaded_image_in_array = img
    # normalize
    loaded_image_in_array=loaded_image_in_array/255

    # add additional dim such as to match input dim of the model architecture
    x = np.expand_dims(loaded_image_in_array, axis=0)

    # prediction
    prediction = model.predict(x)

    results=np.argmax(prediction, axis=1)

    if results==0:
        results="The leaf is diseased cotton leaf"
    elif results==1:
        results="The leaf is diseased cotton plant"
    elif results==2:
        results="The leaf is fresh cotton leaf"
    else:
        results="The leaf is fresh cotton plant"

    return results


def disease(request):
    if request.method=="POST":
        img = Image.open(request.FILES['image']).convert('RGB') 
        open_cv_image = np.array(img)
        image = open_cv_image[:, :, ::-1].copy()
        imageCpy = cv2.resize(image, (224, 224))
        preds = model_predict(imageCpy, model)
        result = preds
        context = {'result':result}
        print(result)
        return render(request,'app/result.html',context)
        

    return render(request,'app/disease.html')