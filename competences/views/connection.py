from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

# [Route("/competences/")]
def connection(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if not request.user.is_authenticated or not request.user.is_superuser:
        user = authenticate(request, username = username, password = password)
    else:
        user = request.user        
    if user is not None:
        login(request, user)
        if user.is_superuser:
            return HttpResponseRedirect("/competences/promotions/")
        return HttpResponseRedirect("/competences/etudiants/" + str(user.id))

    context = {
        "erreur": True,
    }
    return render(request, "competences/connection.html", context = context)
