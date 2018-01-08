from django import forms
from django.core.exceptions import ValidationError

def valida_codigo_postal(value):
    if value < 1 or value > 100:
        raise ValidationError("%s no parece ser una edad... salvo que seas vampiro" % value)


class PersonajeForm(forms.Form):
   name    = forms.CharField(label='Nombre', max_length=60, strip=True,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       'placeholder':'nombre',
                                      })
                            )

   adjetive = forms.CharField(label='adjetivo', max_length=80, required=False)

   age = forms.IntegerField(label='edad', validators=[valida_codigo_postal])
