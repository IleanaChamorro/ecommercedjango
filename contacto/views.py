from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()

    #Recuperacion datos formulario
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        #Si se han rellenado todos los campos
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            #Envio consulta al admin email
            email=EmailMessage("Mensaje desde App Django", 
            "El usuario {} con la direccion {} tiene una consulta: \n\n {}". format(nombre, email, contenido),
            "",["pruebaswebp@gmail.com"],reply_to=[email])
            #Manejo error
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, 'contacto/contacto.html', {'formulario': formulario_contacto})
