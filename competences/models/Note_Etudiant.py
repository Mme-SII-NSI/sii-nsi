from django.db import models
from .Etudiant import Etudiant
from .Question import Question
from django.utils.timezone import now

class Note_Etudiant(models.Model) :
    note = models.IntegerField(default = 0)
    acquis = models.IntegerField(default = 0)
    date = models.DateTimeField('Date Note', default = now)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, default = 0)
    etudiant = models.ForeignKey(Etudiant, on_delete = models.CASCADE, default = 0)
    
    def __str__(self) :
        return str(self.etudiant) + ' | ' + str(self.question)