from django.urls import path
from .views import home, firma, areas, equipo, contacto, casos

urlpatterns = [
    path('', home, name="home"),
    path('firma/', firma, name="firma"), 
    path('areas/', areas, name="areas"),
    path('equipo/', equipo, name="equipo"),
    path('contacto/', contacto, name="contacto"),
    path('casos/', casos, name="casos"),
]