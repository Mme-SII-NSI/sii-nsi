from django.db import models
from .Programme import Programme

class Competence(models.Model) :
    competence = models.CharField(max_length = 200)
    code = models.CharField(max_length = 50)
    sous_competence = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'carte', default = '')
    programme = models.ForeignKey(Programme, on_delete = models.CASCADE)

    def __str__(self) :
        code = self.code + ' ' + str(self.programme)
        return code