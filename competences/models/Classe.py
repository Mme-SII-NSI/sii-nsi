from django.db import models
from .Programme import Programme

class Classe(models.Model) :
    classe = models.CharField(max_length = 50)

    def __str__(self) :
        return self.classe