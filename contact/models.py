from django.db import models

class Contact(models.Model):
    """
        Création de la table contact_contact dans la base de données
    """
    name = models.CharField("votre nom".upper(), max_length=100)
    email = models.EmailField("votre mail".upper(), max_length=100)
    content = models.TextField("votre message".upper())
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
