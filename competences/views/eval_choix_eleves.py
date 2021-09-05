from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .Core import Core

# [Route("promotions/<int:idPromotion>/activites/<int:idActivite>/")]
def eval_choix_eleves(request, idPromotion, idActivite):
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    promotion = Core.promotion(idPromotion)
    activite = Core.activite(idActivite)
    etudiantActivite = Core.etudiantEvalueSurActivite(promotion, activite)
    questions = Core.questionsDeLActivite(activite)
    
    context = {
        "promotion": promotion,
        "activite": activite,
        "questions": questions,
        "etudiantActivite": etudiantActivite,
    }

    return render(request, "competences/eval_choix_eleve.html", context=context)
