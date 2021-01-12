from django.shortcuts import render, redirect
from django.urls import reverse

# NOTA: NOSOTROS EN CADA VISTA ACCEDEMOS A LOS TEMPLATES RESPECTIVOS DE CADA UNA. SIN EMBARGO, EXTENDEMOS EL TEMPLATE "base.html" A CADA UNA DE
# ELLAS, POR LO QUE, NO ESTAMOS ACCEDIENDO NUNCA AL TEMPLATE "base.html" SINO EXTENDENDIENDOLO DIRECTAMENTE CADA ACCEDEMOS A LOS DISTINTOS TEMPLATES.

# NOTA 2: En todos los campos en donde se encuentre "xxxxxxxxx@gmail.com", sustituir por tu email. Ir hasta la parte de abajo del archivo "settings.py" y agregar
# sustituir "xxxxxxxxx@gmail.com" por tu correo y la respectiva contraseña. De esta forma, al clonar el repositorio, verás este proyecto desplegado funcionando al
# 100%.

# Create your views here.
from .forms import EmailForm
from django.core.mail import send_mail

def home(request):
    return render(request, template_name="core/Sto-Corp.html")

def firma(request):
    if request.method == "POST":
        correo_form = EmailForm(data=request.POST)
        if correo_form.is_valid():
            subject = "Bufet de Abogados"
            message = "Somos la mejor compañia, contamos con los mejores abogados."
            email_emisor = "xxxxxxxxx@gmail.com"
            data = correo_form.cleaned_data
            email_destinatario = data["email"]
            send_mail(subject, message, email_emisor, [email_destinatario])
            return redirect(reverse("firma")+"?ok")
    else:
        correo_form = EmailForm()
        return render(request, "core/Firma.html", {"form":correo_form})

def areas(request):
    if request.method == "POST":
        correo_form = EmailForm(data=request.POST)
        if correo_form.is_valid():
            subject = "Bufet de Abogados"
            message = "Somos la mejor compañia, contamos con los mejores abogados."
            email_emisor = "xxxxxxxxx@gmail.com"
            data = correo_form.cleaned_data
            email_destinatario = data["email"]
            send_mail(subject, message, email_emisor, [email_destinatario])
            return redirect(reverse("areas")+"?ok")
    else:
        correo_form = EmailForm()
        return render(request, "core/Areas.html", {"form":correo_form})

def equipo(request):
    if request.method == "POST":
        correo_form = EmailForm(data=request.POST)
        if correo_form.is_valid():
            subject = "Bufet de Abogados"
            message = "Somos la mejor compañia, contamos con los mejores abogados."
            email_emisor = "xxxxxxxxx@gmail.com"
            data = correo_form.cleaned_data
            email_destinatario = data["email"]
            send_mail(subject, message, email_emisor, [email_destinatario])
            return redirect(reverse("equipo")+"?ok")
    else:
        correo_form = EmailForm()
        return render(request, "core/Equipo.html", {"form":correo_form})

from .forms import DatosUsuarioForm
def contacto(request):
    if request.method == "POST" and len(request.POST) == 2:
        correo_form = EmailForm(data=request.POST)
        # Haciendo uso de "correo_form.errors.as_data()" podemos desplegar los errores cometidos en el formulario.
        if correo_form.is_valid():
            subject = "Bufet de Abogados"
            message = "Somos la mejor compañia, contamos con los mejores abogados."
            email_emisor = "xxxxxxxxx@gmail.com"
            data = correo_form.cleaned_data
            email_destinatario = data["email"]
            send_mail(subject, message, email_emisor, [email_destinatario])
            return redirect(reverse("contacto")+"?ok")
    
    elif request.method == "POST" and len(request.POST) == 7: # Dado que son 7 campos los que hay en el formulario de contacto.
        datos_form = DatosUsuarioForm(data=request.POST)
        # Haciendo uso de "datos_form.errors.as_data()" podemos desplegar los errores cometidos en el formulario.
        if datos_form.is_valid():
            data = datos_form.cleaned_data
            subject = "Tienes un nuevo cliente."
            message = f"Cliente: {data['nombre']} {data['apellido']}\nEmail: {data['correo']}\nTeléfono: {data['telefono']}\
            \nCelular: {data['celular'] if data['celular'] else 'No especificado'}\nMensaje: {data['contenido']}"
            email_emisor = "xxxxxxxxx@gmail.com"
            email_destinatario = "xxxxxxxxx@gmail.com"
            send_mail(subject, message, email_emisor, [email_destinatario])
            return redirect(reverse("contacto")+"?okform")

        else:
            return redirect(reverse("contacto")+"?formfailed")

    else:
        correo_form = EmailForm()
        return render(request, "core/Contacto.html", {"form":correo_form})

def casos(request):
    if request.method == "POST":
        correo_form = EmailForm(data=request.POST)
        if correo_form.is_valid():
            subject = "Bufet de Abogados"
            message = "Somos la mejor compañia, contamos con los mejores abogados."
            email_emisor = "xxxxxxxxx@gmail.com"
            data = correo_form.cleaned_data
            email_destinatario = data["email"]
            send_mail(subject, message, email_emisor, [email_destinatario])
            return redirect(reverse("casos")+"?ok")
    else:
        correo_form = EmailForm()
        return render(request, "core/Casos_Estudio.html", {"form":correo_form})
