from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout

# [Route("/competences/deconnection")]
def deconnection(request):

    logout(request)
    context = {
        "erreur": True,
    }
    return HttpResponseRedirect("/competences/")
