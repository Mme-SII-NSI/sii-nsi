from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .Core import Core

# [Route("/competences/promotions/<int:idPromotion>/")]
def eval_activite(request, idPromotion):
    if not request.user.is_authenticated or not request.user.is_superuser :
        return HttpResponseRedirect('/competences/')

    promotion = Core.promotion(idPromotion)
    activites = Core.activitesDuProgramme(promotion.programme)
    devoirs = set(Core.flatten([activite.devoirs for (key, activite) in activites.items()]))
    devoirs = sorted(devoirs, key=str, reverse= True)

    context = {
        "promotion": promotion,
        "activites": activites,
        "devoirs": devoirs
    }
    return render(request, "competences/eval_activite.html", context=context)
