from django import forms

from .models import *



class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = '__all__'

class CorreosFomr(forms.ModelForm):
    class Meta:
        model = Correo
        fields = '__all__'

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

        widgets = {
              'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control col-md-12',
                    'placeholder' : 'ingrese su nombre'
                    
                }
            ),

            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control col-md-12',
                    'placeholder' : 'ingrese su correo'
                    
                }
            ),

            'especialidad': forms.Select(
                attrs={
                    'class': 'form-control col-md-12',
                    'placeholder' : 'ingrese su correo'
                    
                }
            ),

            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control col-md-12',
                    'placeholder' : 'escriba su mensaje'
                    
                }
            ),

        }


        