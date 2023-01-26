from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('',Home, name= 'inicio'),
    path('home',Ini, name= 'home'),
    path('servicios',Servicios, name= 'servicios'),
    path('services',Services, name= 'services'),
    path('nosotros',Nosotros, name= 'nosotros'),
    path('about',About, name= 'about'),
    path('directorio',DirecotiroMedico, name= 'directorio'),
    path('directory',MedicalDirecotiry, name= 'directory'),
    path('lnoticias',LNoticias, name= 'lnoticias'),
    path('nnoticias',NNoticias, name= 'nnoticias'),
    path('testimonios',Testimonios, name= 'testimonios'),
    path('testimonials',Testimonials, name= 'testimonials'),
    path('contacto',Contactos, name= 'contacto'),
    path('contact',Contact, name= 'contact'),
    path('ambulancia',Ambulancia, name= 'ambulancia'),
    path('balon',Balon, name= 'balon'),
    path('cirugia',Cirugia, name= 'cirugia'),
    path('village',Village, name= 'village'),
    path('urgencias',Urgencias, name= 'urgencias'),
    path('consultasv',Consultas, name= 'consultasv'),
    path('sonografia',Sonografia, name= 'sonografia'),


]