from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from ..datasAccess.Access import Access

# [Route("promotions/<int:idPromotion>/activites/<int:idActivite>/")]
def eval_choix_eleves(request, idPromotion, idActivite):
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    promotion = Access.promotion(idPromotion)
    activite = Access.activite(idActivite)
    etudiantActivite = Access.etudiantEvalueSurActivite(promotion, activite)
    questions = Access.questionsDeLActivite(activite)
    
    context = {
        "promotion": promotion,
        "activite": activite,
        "questions": questions,
        "etudiantActivite": etudiantActivite,
    }

    return render(request, "competences/eval_choix_eleve.html", context=context)
