from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from ..models.Etudiant import Etudiant
from ..models.Promotion import Promotion
from ..models.Etudiant_Promotion import Etudiant_Promotion
from ..models.Etudiant_Promotion import Etudiant_Promotion
from ..models.Detail_Competence import Detail_Competence
from .Core import Core

# [Route("/competences/etudiants/<int:idEtudiant>/")]
def bilan_perso(request, idEtudiant):

    if not Etudiant.objects.filter(id= idEtudiant).exists():
        HttpResponseRedirect('/competences/')
    etudiant = Etudiant.objects.get(id= idEtudiant)

    if request.user.id != etudiant.auth_user.id or not request.user.is_authenticated:
        return HttpResponseRedirect('/competences/')

    promotionsDeEtudiant = Core.promotionsDeEtudiant(idEtudiant)
    programme = promotionsDeEtudiant[0].programme
    detailCompetences = Detail_Competence.objects.filter(programme_id= programme.id)

    dic = {}
    for detailCompetence in detailCompetences:
        if detailCompetence.theme not in dic:
            dic[detailCompetence.theme] = {}
        if detailCompetence.competence not in dic[detailCompetence.theme]:
            dic[detailCompetence.theme][detailCompetence.competence] = []
        dic[detailCompetence.theme][detailCompetence.competence].append(detailCompetence)


    context = {
        'etudiant' : etudiant,
        'promotions' : promotionsDeEtudiant,
        'dic' : dic
    }
    return render(request, 'competences/bilan_perso.html', context=context)