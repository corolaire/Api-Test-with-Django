from rest_framework import serializers
from .models import animals,userdatacomplete,species,login,race

class serializeranimals(serializers.ModelSerializer): 
    class Meta:
        model=animals #modelo con el cual vamos a trabajar
        fields=['age','hair_color','eyes_color','weight','character','teeth','size','diseases','disabilities']# campos (columnas a mi entender)django genera automatic.pk a los campos
        # el id pk esta en la base de datos directamente con django
        
        
class serializeruserdatacomplete(serializers.ModelSerializer):
    class Meta:
        model=userdatacomplete
        fields=['name','lastname','numberphone','email','age']
        
class serializerspecies(serializers.ModelSerializer):
    class Meta:
        model=species
        fields=['species_name']

class serializerlogin(serializers.ModelSerializer):
    class Meta:
        model=login
        fields=['user_email','user_password','cellphonenumber','user_name','is_active']
        
class serializerrace(serializers.ModelSerializer):
    class Meta:
        model=race
        fields=['race_name']