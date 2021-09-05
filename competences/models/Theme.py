from django.db import models
from .Programme import Programme

class Theme(models.Model) :
    theme = models.CharField(max_length = 50)
    programme = models.ForeignKey(Programme, on_delete = models.CASCADE)

    def __str__(self) :
        return self.theme