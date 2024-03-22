from django.http.request import HttpHeaders, HttpRequest
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from fastapi.responses import HTMLResponse

# Create your views here.


def index(request: HttpRequest):
    return render(request, "spa/index.html")


def section(request: HttpRequest, page: int):
    if 0 < page and page <= 5:
        return HttpResponse(f"<h1> Landing Page is {page:>4}</h1>" * page)
    else:
        return Http404("Page Not Found.")
