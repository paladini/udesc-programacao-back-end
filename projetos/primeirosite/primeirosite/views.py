from django.http import HttpRequest, HttpResponse

def index(request):
    """
    View function for the home page of the site.
    """
    return HttpResponse("Olá, mundo! Pela enésima vez.")