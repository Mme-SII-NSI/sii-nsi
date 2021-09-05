from django.db import models
from .Promotion import Promotion
from .Etudiant import Etudiant

class Etudiant_Promotion(models.Model) :
    promotion = models.ForeignKey(Promotion, on_delete = models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete = models.CASCADE)
    
    def __str__(self) :
        return str(self.promotion) + ' | ' + str(self.etudiant)
    