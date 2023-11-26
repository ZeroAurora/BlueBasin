from django.http import HttpRequest

from .models import Identity


def identity(request: HttpRequest) -> dict:
    def current():
        if idpk := request.session.get("identity", None):
            return Identity.objects.filter(pk=idpk).first()

    def all():
        return Identity.objects.filter(user=request.user)

    def available():
        return Identity.objects.filter(user=request.user, deprecated_at=None)

    return {
        "identity": {
            "current": current,
            "all": all,
            "available": available,
        }
    }
