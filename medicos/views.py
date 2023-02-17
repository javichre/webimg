from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from email import message
from django.contrib import messages
from django.views.generic import TemplateView,View,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .forms import *
from .models import *


def Home(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        Correo.objects.create(correo  = email)
    return render(request,'index.html' )
    #return render(request,'index.html' )


def Ini(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        Correo.objects.create(correo  = email)
    return render(request,'en/home.html' )

def Contactos(request):
    if request.method == 'POST':
        captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        contacto =  ContactoForm(request.POST)
        if contacto.is_valid():
            contacto.save()
            messages.success(request,"Contacto agregado exitosamente")  
            return redirect('inicio')
    else:
        contacto = ContactoForm()
    
    return render(request,'contacto.html', {'contacto':contacto} )



def Contact(request):
    if request.method == 'POST':
        contacto =  ContactoForm(request.POST)
        if contacto.is_valid():
            contacto.save()
            messages.success(request,"Contacto agregado exitosamente")  
            return redirect('home')
    else:
        contacto = ContactoForm()
    
    return render(request,'en/contact.html', {'contacto':contacto} )


class Contacto(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('inicio')

def Servicios(request):
    return render(request,'servicios.html')

def Services(request):
    return render(request,'en/services.html')

def Ambulancia(request):
    return render(request,'servicios/ambulancia.html')


def Balon(request):
    return render(request,'servicios/balon.html')

def Cirugia(request):
    return render(request,'servicios/cirugia_general.html')


def Nosotros(request):
    return render(request,'nosotros.html')

def About(request):
    return render(request,'en/about.html')


def Testimonios(request):
    return render(request,'testimonios.html')


def Testimonials(request):
    return render(request,'en/testimonials.html')

def DirecotiroMedico(request):
    anesteciologos = Medico.objects.filter(especialidad_id = 1)
    cardiologos = Medico.objects.filter(especialidad_id = 2)
    cirujanos = Medico.objects.filter(especialidad_id = 3)
    nutriologos = Medico.objects.filter(especialidad_id = 4)
    gastro = Medico.objects.filter(especialidad_id = 5)
    endocrinología = Medico.objects.filter(especialidad_id = 6)
    ginecologia = Medico.objects.filter(especialidad_id = 7)
    internistas = Medico.objects.filter(especialidad_id = 8)
    oftalmología = Medico.objects.filter(especialidad_id = 9)
    otorrinolaringología = Medico.objects.filter(especialidad_id = 10)
    pediatria = Medico.objects.filter(especialidad_id = 11)
    psicología = Medico.objects.filter(especialidad_id = 12)
    radiología = Medico.objects.filter(especialidad_id = 13)
    ortopedia = Medico.objects.filter(especialidad_id = 14)
    fisiatría =  Medico.objects.filter(especialidad_id = 15)
    urología =  Medico.objects.filter(especialidad_id = 16)

    return render(request,'medicos/listado_medicos.html' , {'anesteciologos':anesteciologos,'cardiologos':cardiologos,'cirujanos':cirujanos,
    'nutriologos':nutriologos,'gastro':gastro,'endocrinología':endocrinología,'ginecologia':ginecologia,'internistas':internistas,
    'oftalmología':oftalmología,'otorrinolaringología':otorrinolaringología,'pediatria':pediatria,'psicología':psicología,
    'radiología':radiología,'ortopedia':ortopedia,'fisiatría':fisiatría,'urología':urología

    } )


def MedicalDirecotiry(request):
    anesteciologos = Medico.objects.filter(especialidad_id = 1)
    cardiologos = Medico.objects.filter(especialidad_id = 2)
    cirujanos = Medico.objects.filter(especialidad_id = 3)
    nutriologos = Medico.objects.filter(especialidad_id = 4)
    gastro = Medico.objects.filter(especialidad_id = 5)
    endocrinología = Medico.objects.filter(especialidad_id = 6)
    ginecologia = Medico.objects.filter(especialidad_id = 7)
    internistas = Medico.objects.filter(especialidad_id = 8)
    oftalmología = Medico.objects.filter(especialidad_id = 9)
    otorrinolaringología = Medico.objects.filter(especialidad_id = 10)
    pediatria = Medico.objects.filter(especialidad_id = 11)
    psicología = Medico.objects.filter(especialidad_id = 12)
    radiología = Medico.objects.filter(especialidad_id = 13)
    ortopedia = Medico.objects.filter(especialidad_id = 14)
    fisiatría =  Medico.objects.filter(especialidad_id = 15)
    urología =  Medico.objects.filter(especialidad_id = 16)

    return render(request,'en/medicos/list_doctors.html' , {'anesteciologos':anesteciologos,'cardiologos':cardiologos,'cirujanos':cirujanos,
    'nutriologos':nutriologos,'gastro':gastro,'endocrinología':endocrinología,'ginecologia':ginecologia,'internistas':internistas,
    'oftalmología':oftalmología,'otorrinolaringología':otorrinolaringología,'pediatria':pediatria,'psicología':psicología,
    'radiología':radiología,'ortopedia':ortopedia,'fisiatría':fisiatría,'urología':urología

    } )

def NNoticias(request):
    if request.method == "POST":
        
        
        fecha = request.POST.get('fecha')
        encabezado = request.POST.get('encabezado')
        texto = request.POST.get('texto')
        comentario = request.POST.get('comentario')
        images = request.FILES.getlist('imagen')
        


        for imagen in images:
            Noticias.objects.create(imagen= imagen,fecha = fecha, encabezado = encabezado, texto = texto, comentario = comentario )
        uploaded_images = Noticias.objects.all()
        return redirect('lnoticias')
        #return JsonResponse({"images": [{"url": picture.picture.url} for picture in uploaded_images]})
        
    return render(request, "noticias/nueva_noticia.html")

def NNoticas(request):
    if request.method == 'POST':
        noticia = NoticiasForm(request.POST,files=request.FILES)
        if noticia.is_valid():
            noticia.save()
            return redirect('lnoticias')
    else:
        noticia = NoticiasForm()
    
    return render(request,'noticas')




def LNoticias(request):
    noticias = Noticias.objects.all()
    return render(request,'noticias/listado_noticias.html' , {'noticias':noticias} )



def Village(request):
    return render(request,'village.html')

def Urgencias(request):
    return render(request,'urgencias.html')

def Consultas(request):
    return render(request,'consultasv.html')


def Sonografia(request):
    return render(request,'sonografia.html')