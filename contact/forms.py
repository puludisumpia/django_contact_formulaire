from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):
    """
        Création du formualire à partir du model Contact
    """
    class Meta:
        model = Contact
        fields = ("name", "email", "content",)