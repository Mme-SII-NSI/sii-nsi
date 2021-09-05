from django.db import models

class Programme(models.Model) :
   titre = models.CharField(max_length = 20)

   def __str__(self) :
       return self.titre