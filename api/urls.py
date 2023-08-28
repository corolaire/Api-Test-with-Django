from django.urls import path,include #
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'animals',views.animalsViewSet)#va a tener la o las rutas correspondientes a animals
router.register(r'login',views.loginViewSet)
router.register(r'race',views.raceViewSet)
router.register(r'species',views.speciesViewSet)
router.register(r'userdatacomplete',views.userdatacompleteViewSet) 

urlpatterns = [
    path('',include(router.urls)) #va a contener todas las rutas que arriba le registramos
]

#estan ya creadas todas las rutas para cada modelo a partir de viewset de las vistas
#maneja todas las vista correspondientes del modelo .
#la r es importante porque la r evita que lo interprete como un salto de linea o tabulacion