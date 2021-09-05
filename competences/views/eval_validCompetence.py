from django.shortcuts import HttpResponseRedirect
from django.db.models.functions import Now
from ..models.Etudiant import Etudiant
from ..models.Question import Question
from ..models.Note_Etudiant import Note_Etudiant
from .Core import Core

# [Route("/competences/promotions/<int:idPromotion>/activites/<int:idActivite>/etudiants/<int:idEtudiant>/validation/")]
def eval_validCompetence(request, idPromotion, idActivite, idEtudiant) :
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    questionIds = request.POST.getlist("ref", False)
    etudiant = Etudiant.objects.get(id= idEtudiant)
    for questionId in questionIds :
        question = Question.objects.get(id= questionId)
        note = request.POST.get('point' + questionId, '0')
        acquis = request.POST.get('valid' + questionId, '0')
        noteEtudiant = Note_Etudiant.objects.get_or_create(etudiant_id= etudiant.id, question_id= question.id)[0]
        noteEtudiant.note = int(note)
        noteEtudiant.acquis = int(acquis)
        noteEtudiant.etudiant_id = etudiant.id
        noteEtudiant.question_id = question.id 
        noteEtudiant.date = Now()
        noteEtudiant.save()

    adresseRedirection = '/competences/promotions/'+ str(idPromotion) + '/activites/' + str(idActivite) + '/etudiants/' + str(idEtudiant)
    return HttpResponseRedirect(adresseRedirection)