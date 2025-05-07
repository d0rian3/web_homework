from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render


def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')


def my_feed(request: HttpRequest) -> HttpResponse:
    return render(request, 'my_feed.html')

def article(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page on which the id article will be displayed.") #! Page


def article_comment(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The address we will use to write comments to the article")

def article_update(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page we will use to modify an existing article.") #! Page


def article_delete(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The address we will use to delete the article")


def create(request: HttpRequest) -> HttpResponse:
    return render(request, 'create.html')

def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page listing all the topics on the site") #! Page

def topic_id(request: HttpRequest) -> HttpResponse:
    return HttpResponse(" Страница, со всеми статьями по определенной теме") #! Page

def topic_id_subscribe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page listing all topics on the site Address to subscribe to a specific topic") #! Page


def topic_id_unsubscribe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page listing all topics on the site Address to unsubscribe to a specific topic") #! Page

def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'profile.html')
def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'register.html')

def set_password(request: HttpRequest) -> HttpResponse:
    return render(request, 'set_pass.html')

def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Address for leaving the site")

def data_sort(request: HttpRequest, year:int, month: int) -> HttpResponse:
    try:
        year = int(year)
        month = int(month)
        if not 1900 <= year <= 2100:
            raise ValueError("Year outside the acceptable range")
        if not 1 <= month <= 12:
            raise ValueError("The month must be between 1 and 12")
        

    except(ValueError, TypeError):
        raise Http404("Incorrect date")
    return render(request, 'data_sort.html', {'year': year, 'month': month})
    