from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            content = form.cleaned_data.get("content")

            # sauvegarde dans la base de données
            new_contact = Contact(
                name=name,
                email=email,
                content=content
            )
            new_contact.save()


            # Envoi email de confirmation 
            subject = "Confirmation reception de votre message"
            body = f"""
                        Bonjour {name},
                        Nous avons bien reçu votre message, et nous mettons
                        tout en oeuvre pour vous répondre dans les meilleurs délais.
                   """

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            messages.success(
                request,
                "Votre message a été envoyé avec succès",
                "success"
            )
            return redirect("contact")

        else:
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})



""""
    Codé par Mpia Mimpiya P.
"""