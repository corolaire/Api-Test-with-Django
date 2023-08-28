from django.db import models

# Create your models here.
class animals(models.Model):
    age=models.PositiveSmallIntegerField()
    hair_color=models.CharField(max_length=20)
    eyes_color=models.CharField(max_length=20)
    weight=models.PositiveSmallIntegerField()
    character=models.CharField(max_length=20)
    teeth=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    diseases=models.CharField(max_length=100)
    disabilities=models.CharField(max_length=100)
    
    
    
class login(models.Model):
    user_email=models.CharField(max_length=20)
    user_password=models.CharField(max_length=20)
    cellphonenumber=models.PositiveSmallIntegerField()
    user_name=models.CharField(max_length=16)
    is_active=models.BooleanField(default=True)
    
    
class race(models.Model):
    race_name=models.CharField(max_length=20)
    
    
class species(models.Model):
    species_name=models.CharField(max_length=20)
    
class userdatacomplete(models.Model):
    name=models.CharField(max_length=15)
    lastname=models.CharField(max_length=20)
    numberphone=models.PositiveSmallIntegerField()
    email=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    
    
    

    
