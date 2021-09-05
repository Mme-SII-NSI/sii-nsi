from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .Core import Core

# [Route("/competences/promotions/<int:idPromotion>/activites/<int:idActivite>/etudiants/<int:idEtudiant>/")]
def eval_competences(request, idPromotion, idActivite, idEtudiant):
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    promotion = Core.promotion(idPromotion)
    activite = Core.activite(idActivite)
    etudiantActivite = Core.etudiantEvalueSurActivite(promotion, activite)
    questions = Core.questionsDeLActivite(activite)
    Core.noteEtudiant(questions, idEtudiant)

    context = {
        "promotion": promotion,
        "activite": activite,
        "questions": questions,
        "etudiantActivite": etudiantActivite,
        "idEtudiant": idEtudiant
    }
    return render(request, "competences/eval_competences.html", context=context)
