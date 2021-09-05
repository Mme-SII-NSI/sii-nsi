from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from ..datasAccess.Access import Access

# [Route("/competences/promotions/<int:idPromotion>/activites/<int:idActivite>/etudiants/<int:idEtudiant>/")]
def eval_competences(request, idPromotion, idActivite, idEtudiant):
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    promotion = Access.promotion(idPromotion)
    activite = Access.activite(idActivite)
    etudiantActivite = Access.etudiantEvalueSurActivite(promotion, activite)
    questions = Access.questionsDeLActivite(activite)
    Access.noteEtudiant(questions, idEtudiant)

    context = {
        "promotion": promotion,
        "activite": activite,
        "questions": questions,
        "etudiantActivite": etudiantActivite,
        "idEtudiant": idEtudiant
    }
    return render(request, "competences/eval_competences.html", context=context)
