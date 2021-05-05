from django import forms

CONTINENT = [
    ("Afrique", "Afrique"),
    ("Europe", "Europe"),
    ("Amérique", "Amérique"),
    ("Asie", "Asie")
]

SEXE = [
    ("Femme", "Femme"),
    ("Homme", "Homme")
]

AGE = [
    ("Entre 18 et 30 ans", "Entre 18 et 30 ans"),
    ("Entre 31 et 60 ans", "Entre 31 et 60 ans"),
    ("Entre 61 ans et plus", "Entre 61 ans et plus"),
]

class ContactForm(forms.Form):
    name = forms.CharField(label="Votre nom".upper())
    email = forms.EmailField(label="Votre mail".upper())
    continent = forms.ChoiceField(label="Votre continent".upper(), choices=CONTINENT, widget=forms.Select)
    sexe = forms.ChoiceField(label="Votre sexe".upper(), choices=SEXE, widget=forms.RadioSelect)
    age = forms.ChoiceField(label="Votre age".upper(), choices=AGE, widget=forms.Select)
    content = forms.CharField(label="Votre message".upper(), widget=forms.Textarea)
    approuve = forms.BooleanField(label="Accepter les conditions d'utilisations")
    