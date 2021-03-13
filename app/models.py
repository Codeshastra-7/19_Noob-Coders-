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
    deliver = models.ForeignKey(Locations, related_name='loc', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

 