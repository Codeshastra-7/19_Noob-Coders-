from django.shortcuts import render
from app.models import *

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def dashboard(request, id):
    user = Aadhar.objects.get(id=id)
    driver = Driver.objects.filter(contact = user)
    context = {
        'apikey': 'AIzaSyCYUeS2YnGYNzt9kZRc1p-4tt4IyEacsjY',
        'user': user,
        'driver': driver

    }
    return render(request,'app/dashboard.html',context)