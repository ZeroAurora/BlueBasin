from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import render

from .models import Identity


@login_required
def index(request: HttpRequest):
    if request.method == "POST":
        id_field = request.POST.get("identity")
        if id_field == "new":
            newid = Identity(user=request.user)
            newid.save()
            request.session["identity"] = newid.pk
        else:
            if Identity.objects.filter(pk=id_field).first().user == request.user:
                request.session["identity"] = id_field
            else:
                return HttpResponseForbidden()
    return render(request, "identity/index.html")
