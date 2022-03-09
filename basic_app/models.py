from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    bdate=models.DateField(null=True,blank=True)
    country=models.ForeignKey('Country',on_delete=models.CASCADE)
    state=models.ForeignKey('State',on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    city=models.ForeignKey('City',on_delete=models.CASCADE)


class Country(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    city = models.ForeignKey('District', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name
