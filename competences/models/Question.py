from django.db import models
from .Activite import Activite
from .Detail_Competence import Detail_Competence


class Question(models.Model):
    num_question = models.CharField(max_length = 8)
    point = models.IntegerField(default = 0)
    activite = models.ForeignKey(Activite, on_delete = models.CASCADE)
    detail_competence = models.ForeignKey(Detail_Competence, on_delete = models.CASCADE)

    def __str__(self):
        libelle = self.num_question + " " + self.detail_competence.code
        return libelle
