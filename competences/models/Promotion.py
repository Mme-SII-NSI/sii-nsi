from django.db import models
from .Programme import Programme
from .Classe import Classe

class Promotion(models.Model) :
    annee = models.CharField(max_length = 20)
    classe = models.ForeignKey(Classe, on_delete = models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete = models.CASCADE)
    
    def __str__(self) :
        return self.annee + ' ' + str(self.classe)
    