from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect, Http404,HttpRequest

from .models import PlaceCoworking, UsersCoworking
from .service import queryset_optimization
from users.models import User

def home_page_view(request: WSGIRequest):
    # Обязательно! каждая функция view должна принимать первым параметром request.
    all_place_coworking = PlaceCoworking.objects.all()  # Получение всех записей из таблицы этой модели.
    
    #queryset = queryset_optimization(Note.objects.all())
     
    context: dict = {
        "places": all_place_coworking
    }
    
    return render(request, "home.html", context)
    #return render(request, "home.html", {"notes": queryset[:100]})

def users_coworking_page_view(request: WSGIRequest, username: str):
    
    # try:
    #     all_user_coworking = UsersCoworking.objects.get(id=user_id)
    #     context: dict = {
    #         "users_coworking": all_user_coworking
    #     }
    # except UsersCoworking.DoesNotExist:
    #     raise Http404
    # return render(request, "home.html", context)
    
    queryset = queryset_optimization(
        UsersCoworking.objects.filter(users__username=username)
    )
    
    print(UsersCoworking.objects.filter(users__username=username).query)
    
    return render(request, "users-coworking-list.html", {"usercoworkinslist": queryset})
    
    
    
def show_place_view(request: WSGIRequest, place_id):
    try:
        place = PlaceCoworking.objects.get(id=place_id)  # Получение только ОДНОЙ записи.

    except PlaceCoworking.DoesNotExist:
        # Если не найдено такой записи.
        raise Http404
        
    return render(request, "coworking-place.html", {"place": place})
