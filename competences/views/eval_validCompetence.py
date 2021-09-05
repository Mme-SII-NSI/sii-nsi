from django.shortcuts import HttpResponseRedirect
from ..datasAccess.Access import Access

# [Route("/competences/promotions/<int:idPromotion>/activites/<int:idActivite>/etudiants/<int:idEtudiant>/validation/")]
def eval_validCompetence(request, idPromotion, idActivite, idEtudiant) :
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    idsQuestion = request.POST.getlist("ref", False)
    for idQuestion in idsQuestion :
        note = request.POST.get('point' + idQuestion, '0')
        acquis = request.POST.get('valid' + idQuestion, '0')
        Access.creationOuMajNoteEtudiant(idEtudiant, idQuestion, note, acquis)

    adresseRedirection = '/competences/promotions/'+ str(idPromotion) + '/activites/' + str(idActivite) + '/etudiants/' + str(idEtudiant)
    return HttpResponseRedirect(adresseRedirection)