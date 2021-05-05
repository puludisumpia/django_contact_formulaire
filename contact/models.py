from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    continent = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    content = models.TextField()
    approuve = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
