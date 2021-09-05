from django.db import models
from .Competence import Competence
from .Theme import Theme
from .Programme import Programme

class Detail_Competence(models.Model) :
    titre = models.CharField(max_length = 200)
    code = models.CharField(max_length = 50)
    competence = models.ForeignKey(Competence, on_delete = models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete = models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete = models.CASCADE)

    def __str__(self) :
        return self.titre

