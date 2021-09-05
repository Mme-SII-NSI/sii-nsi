from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.bilan_perso import bilan_perso
from .views.eval_activite import eval_activite
from .views.eval_choix_eleves import eval_choix_eleves
from .views.eval_competences import eval_competences
from .views.eval_validCompetence import eval_validCompetence
from .views.listePromotions import listePromotions
from .views.connection import connection
from .views.deconnection import deconnection

urlpatterns = [
    # Login
    path("", connection, name="connection"),
    path("deconnection/", deconnection, name="deconnection"),
    path("promotions/", listePromotions, name="promotions"),

    # Evaluations
    path("promotions/<int:idPromotion>/", eval_activite, name="eval_activite",),
    path("promotions/<int:idPromotion>/activites/<int:idActivite>/", eval_choix_eleves, name="eval_choix_eleves",),
    path("promotions/<int:idPromotion>/activites/<int:idActivite>/etudiants/<int:idEtudiant>/", eval_competences, name="eval_competences",),
    path("promotions/<int:idPromotion>/activites/<int:idActivite>/etudiants/<int:idEtudiant>/validation/", eval_validCompetence, name="eval_validCompetence",),
    
    # Etudiants
    path("etudiants/<int:idEtudiant>/", bilan_perso, name="bilan_perso", ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
