from django.shortcuts import render
from app.models import *
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response 
from django.contrib import messages
from geopy.distance import geodesic


# Create your views here.
def index(request):
    return render(request,'app/index.html')

def dashboard(request, id):
    user = Aadhar.objects.get(id=id)
    driver = Driver.objects.filter(contact = user)
    details = WareHouse.objects.filter(farmer = user)[0]
    context = {
        #'apikey': 'AIzaSyCYUeS2YnGYNzt9kZRc1p-4tt4IyEacsjY',
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
        })
        context.append(li)        
    return Response({"message":"success", "data": context})


    
