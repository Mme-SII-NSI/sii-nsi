from django.db.models.functions import Now
from ..models.Etudiant_Promotion import Etudiant_Promotion
from ..models.Activite import Activite
from ..models.Programme import Programme
from ..models.Question import Question
from ..models.Theme import Theme
from ..models.Promotion import Promotion
from ..models.Note_Etudiant import Note_Etudiant
from ..models.Etudiant import Etudiant
from ..models.Competence import Competence
from ..models.Detail_Competence import Detail_Competence
from .Range import Range
from .ActiviteDic import ActiviteDic

class Access:

    def questionsDeLActivite(activite):
        """Renvoie un dictionnaire propre à l'activité code dont la clé est le numéro de la question, et la valeur est la compétence."""
        
        questions = activite.question_set.all()
        for question in questions:
            question.range = Range(question.point)
            question.acquis = ''
        return questions

    def noteEtudiant(questions, idEtudiant):
        """Récupère les notes de l'utilisateurs."""
        
        questionsIds = [ question.id for question in questions ]
        notes = Note_Etudiant.objects\
            .filter(question_id__in= questionsIds)\
            .filter(etudiant_id= idEtudiant)
        for question in questions:
            for note in notes:
                if question.id == note.question.id:
                    question.range.setNote(note.note)
                    question.acquis = 'checked' if note.acquis == 1 else ''
                    break
        return questions


    def creationOuMajNoteEtudiant(idEtudiant, idQuestion, note, acquis):
        question = Question.objects.get(id= idQuestion)
        etudiant = Etudiant.objects.get(id= idEtudiant)
        noteEtudiant = Note_Etudiant.objects.get_or_create(etudiant_id= etudiant.id, question_id= question.id)[0]
        noteEtudiant.note = int(note)
        noteEtudiant.acquis = int(acquis)
        noteEtudiant.etudiant_id = etudiant.id
        noteEtudiant.question_id = question.id 
        noteEtudiant.date = Now()
        noteEtudiant.save()

    def listeDesPromotions():
        """Renvoie la liste des promotions (niveau et année)"""

        dic = {}
        promotions = Promotion.objects.all()
        for promotion in promotions:
            if promotion.classe.classe not in dic:
                dic[promotion.classe.classe] = [] 
            dic[promotion.classe.classe].append(promotion)
            dic[promotion.classe.classe].sort(key=str, reverse= True)
        return dic

    def promotion(idPromotion):
        """Renvoie la promotion"""
        return Promotion.objects.get(id= idPromotion)

    def activite(idActivite):
        """Renvoie l'activite'"""
        return Activite.objects.get(id= idActivite)

    def etudiantEvalueSurActivite(promotion, activite):
        """Renvoie la liste des élèves avec si oui ou non evalue"""

        etudiants_promo = Etudiant_Promotion.objects.filter(promotion_id= promotion.id)
        etudiants = [etudiant_promo.etudiant for etudiant_promo in etudiants_promo]
        questions = Question.objects.all().filter(activite_id= activite.id)
        questionIds = [question.id for question in questions]
        
        for etudiant in etudiants:
            evalue = Note_Etudiant.objects\
                .filter(etudiant_id= etudiant.id)\
                .filter(question_id__in= questionIds)\
                .exists()
            etudiant.evalue = evalue
        return etudiants

    def promotionsDeEtudiant(idEtudiant):
        promotions = [ Etudiant_Promotion.promotion for Etudiant_Promotion in Etudiant_Promotion.objects.filter(etudiant_id= idEtudiant)]
        promotions.sort(key=str, reverse= True)
        return promotions

    def elevesDeLaPromotion(classe, programme, annee):
        """Renvoie la liste des élèves issu d'un niveau (MP/MPSI/etc.), et d'une année"""

        promotion = Promotion.objects\
            .filter(annee= annee)\
            .filter(classe__classe= classe)\
            .filter(classe__programme__titre= programme)
        
        return [eleve.utilisateur for eleve in promotion]

    def themesDuProgramme(programme):
        """Renvoie la liste des différents thèmes du programme"""

        return Theme.objects.filter(programme_id= programme.id)

    def activitesDuProgramme(programme: Programme):
        """Renvoie un dictionnaire dont la clé est le thème et la valeur est la liste de l'ensemble des activités se rapportant au programme"""

        themes = Theme.objects.filter(programme_id= programme.id)
        devoirs = set()
        liste_act = {}
        for theme in themes:
            liste_act[theme.theme] = ActiviteDic()
        
        activites = Activite.objects.filter(programme_id= programme.id)
        for activite in activites:
            themes = set(activite.question_set.all().values_list("detail_competence__theme__theme"))
            for theme in themes:
                liste_act[theme[0]].add(activite)

        devoirs = set(Access.flatten([activite.devoirs for (key, activite) in liste_act.items()]))
        devoirs = sorted(devoirs, key=str, reverse= True)                
        return liste_act, devoirs

    def flatten(t):
        """Applati une liste de liste en liste"""
        return [item for sublist in t for item in sublist]



