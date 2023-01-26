from django.db import models

# Create your models here.

class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=100, blank=False,null=False)

    def __str__(self):
        return self.sexo

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=100, blank=False,null=False)

    def __str__(self):
        return self.especialidad

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField('Imagen de Perfil',upload_to="doctores/", null= False,blank = False)
    especialidad = models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    sexo =  models.ForeignKey(Sexo,on_delete=models.CASCADE)
    nombres  = models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self.nombres

class Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    encabezado = models.CharField(max_length=1000, null=False, blank=False)
    texto = models.CharField(max_length=10000, null=False, blank=False)
    comentario = models.CharField(max_length=10000, null=True, blank=True)
    imagen = models.ImageField('Imagen de portada',upload_to="noticas/", null= False,blank = False)

    def __str__(self):
        return self.encabezado

class Correo(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField()

    def __str__(self):
        return self.correo

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombres  = models.CharField(max_length=100, null=False,blank=False)
    correo = models.EmailField()
    especialidad = models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    mensaje  = models.CharField(max_length=100, null=False,blank=False)


    def __str__(self):
        return self.nombres


class Seguros(models.Model):
    id = models.AutoField(primary_key=True)
    seguro  = models.CharField(max_length=100, null=False,blank=False)
    imagen = models.ImageField('Imagen de Perfil',upload_to="seguros/", null= False,blank = False)

    def __str__(self):
        return self.seguro

class Portada(models.Model):
    id = models.AutoField(primary_key=True)
    portada  = models.CharField(max_length=100, null=False,blank=False)
    imagen = models.ImageField('Imagen de Perfil',upload_to="seguros/", null= False,blank = False)

    def __str__(self):
        return self.portada
