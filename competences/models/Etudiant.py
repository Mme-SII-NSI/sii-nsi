from django.db import models
from django.contrib.auth.models import User
from .Classe import Classe

class Etudiant(models.Model) :
    nom = models.CharField(max_length = 100)
    prenom = models.CharField(max_length = 100)
    auth_user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self) :
        etudiant = self.nom + ' ' + self.prenom
        return etudiant