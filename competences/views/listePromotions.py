from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .Core import Core

# [Route("/competences/promotions")]
def listePromotions(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return HttpResponseRedirect('/competences/')

    promotions = Core.listeDesPromotions()
    context = {
        "promotions": promotions,
    }
    return render(request, "competences/listePromotions.html", context=context)
