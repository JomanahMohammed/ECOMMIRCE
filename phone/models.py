from django.db import models

# Create your models here.

class Items(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ItemDetails(models.Model):
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    image=models.CharField(max_length=150)
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.price


class Cart(models.Model):
    Id_proudct=models.IntegerField()
    Id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)


class Device(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class DeviceDetails(models.Model):
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    image=models.CharField(max_length=150)
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Device,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.price



