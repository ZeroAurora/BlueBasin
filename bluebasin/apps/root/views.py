from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def markdown(request):
    return render(request, "markdown.html")


def welcome(request):
    return render(request, "welcome.html")


def code_of_conduct(request):
    return render(request, "code_of_conduct.html")


def terms(request):
    return render(request, "terms.html")
