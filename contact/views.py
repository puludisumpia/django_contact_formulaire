from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .forms import ContactForm


def contacter(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            continent = form.cleaned_data.get("continent")
            sexe = form.cleaned_data.get("sexe")  
            age = form.cleaned_data.get("age")
            content = form.cleaned_data.get("content")    
            approuve = True if form.cleaned_data.get("approuve") else False

            new_contact = Contact(
                name=name.upper(),
                email=email,
                continent=continent,
                sexe=sexe,
                age=age,
                content=content,
                approuve=approuve
            )
            new_contact.save()

            subject = "Confirmation reception message"
            corps = f"""
                Bonjour {name},
                Nous avons bien reçu votre message et
                nous mettons tout en oeuvre pour vous 
                répondre dans les meilleurs délais.
            """
            send_mail(
                subject,
                corps,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            messages.success(
                request,
                "Votre message a été envoyé avec succès",
                "success"
            )
            return redirect(contacter)
        else:
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
