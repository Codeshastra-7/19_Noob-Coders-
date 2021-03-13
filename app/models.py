from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadharno = models.CharField(max_length=16)
    image = models.ImageField(upload_to="aadhar")
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    verified = models.BooleanField(default=False)


    def __str__(self):
        return str(self.aadharno)


class Locations(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to="location")

    def __str__(self):
        return str(self.name)

class WareHouse(models.Model):
    farmer = models.ForeignKey(Aadhar,on_delete=models.CASCADE)
    instockkgs = models.IntegerField()
    outfordeliverykgs = models.FloatField()
    currentcottonprice = models.FloatField()
    monthlyrevenue = models.FloatField()

class Driver(models.Model):
    contact = models.ForeignKey(Aadhar, related_name="user", on_delete=models.CASCADE)
    name= models.CharField(max_length=150, blank=True, null=True)
    currentdetails = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    truckno =  models.CharField(max_length=150, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="drivers")
    deliver = models.ForeignKey(Locations, related_name='loc', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)


class TransportItems(models.Model):
    farmer = models.ForeignKey(Aadhar, related_name='aadhar',on_delete=models.CASCADE,null=True, blank=True)
    quantity = models.FloatField(null=True)
    drive = models.ForeignKey(Driver, related_name='driver_name', on_delete=models.DO_NOTHING,null=True,blank=True)
    time_created = models.DateField(auto_now_add=True)
    dispatchtime = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=300,null=True, blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.farmer.name)


 