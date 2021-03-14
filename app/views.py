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
    return render(request, 'app/marketplace.html')