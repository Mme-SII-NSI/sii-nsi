from django.contrib import admin

# Register your models here.
from .models.Activite import Activite
from .models.Classe import Classe
from .models.Competence import Competence
from .models.Detail_Competence import Detail_Competence
from .models.Note_Etudiant import Note_Etudiant
from .models.Programme import Programme
from .models.Promotion import Promotion
from .models.Etudiant_Promotion import Etudiant_Promotion
from .models.Question import Question
from .models.Theme import Theme
from .models.Etudiant import Etudiant

admin.site.register(Activite)
admin.site.register(Classe)
admin.site.register(Competence)
admin.site.register(Detail_Competence)
admin.site.register(Note_Etudiant)
admin.site.register(Programme)
admin.site.register(Promotion)
admin.site.register(Etudiant_Promotion)
admin.site.register(Question)
admin.site.register(Theme)
admin.site.register(Etudiant)


