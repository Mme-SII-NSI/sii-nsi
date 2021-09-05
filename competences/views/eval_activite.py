from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from ..datasAccess.Access import Access

# [Route("/competences/promotions/<int:idPromotion>/")]
def eval_activite(request, idPromotion):
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    promotion = Access.promotion(idPromotion)
    activites, devoirs = Access.activitesDuProgramme(promotion.programme)
    context = {
        "promotion": promotion,
        "activites": activites,
        "devoirs": devoirs
    }
    return render(request, "competences/eval_activite.html", context=context)
