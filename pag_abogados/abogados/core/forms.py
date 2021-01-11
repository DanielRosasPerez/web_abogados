from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(attrs={"placeholder":"daniel123@gmail.com", 
    "style":"padding-left:1%"}))

from phonenumber_field.formfields import PhoneNumberField
class DatosUsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    correo = forms.EmailField(required=True)
    telefono = PhoneNumberField(required=True)
    celular = PhoneNumberField(required=False)
    contenido = forms.CharField(max_length=500)
