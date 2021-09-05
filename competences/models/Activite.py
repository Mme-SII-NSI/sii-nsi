from django.db import models
from .Programme import Programme

class Activite(models.Model) :

    titre = models.CharField(max_length = 200)
    code = models.CharField(max_length = 20)
    type = models.CharField(max_length = 50)
    lien_pdf = models.CharField(max_length = 200)
    programme = models.ForeignKey(Programme, on_delete = models.CASCADE)

    def __str__(self) :
        activite = self.code + ' ' + self.titre
        return activite

    def estDevoir(self):
        return self.type == 'Devoir'