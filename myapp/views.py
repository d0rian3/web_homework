from django.http import HttpResponse, HttpRequest, Http404


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hey! It's your main view!!")

def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page that will only have articles on topics the user is subscribed to.")

def article(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page on which the id article will be displayed.")

def article_comment(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The address we will use to write comments to the article")

def article_update(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page we will use to modify an existing article.")


def article_delete(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The address we will use to delete the article")


def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse(" The page where we will create new articles.")

def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page listing all the topics on the site")

def topics_id(request: HttpRequest) -> HttpResponse:
    return HttpResponse(" Страница, со всеми статьями по определенной теме")

def topics_id_subscribe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page listing all topics on the site Address to subscribe to a specific topic")


def topics_id_unsubscribe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page listing all topics on the site Address to unsubscribe to a specific topic")

def profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("A page with user data and a list of subscriptions")

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("New user registration page")

def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page with the password change")

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Page, for logging into the site")

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
    return HttpResponse(f"A page that will have articles created in a particular month.{month}/{year}")
    