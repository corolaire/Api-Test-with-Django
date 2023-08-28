from rest_framework import viewsets
from .serializer import serializeranimals,serializerlogin,serializerrace,serializerspecies,serializeruserdatacomplete
#importa los serializadore y debajo importa el modelo(en mi caso son varios modelos)
from .models import animals,login,race,species,userdatacomplete


class animalsViewSet(viewsets.ModelViewSet):#aca desarrollamos el query set , vamos a acceder a los elementos mediante la orm de django.
    queryset=animals.objects.all() #los enlista para poder acceder a los elementos de una tabla
    serializer_class=serializeranimals
    
class loginViewSet(viewsets.ModelViewSet):
    queryset=login.objects.all()
    serializer_class=serializerlogin
    
class raceViewSet(viewsets.ModelViewSet):
    queryset=race.objects.all()
    serializer_class=serializerrace
    
class speciesViewSet(viewsets.ModelViewSet):
    queryset=species.objects.all()
    serializer_class=serializerspecies

class userdatacompleteViewSet(viewsets.ModelViewSet):
    queryset=userdatacomplete.objects.all() 
    serializer_class=serializeruserdatacomplete
    
    


# Create your views here.
