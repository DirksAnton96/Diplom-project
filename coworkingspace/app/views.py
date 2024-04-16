from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect, Http404,HttpRequest

from .models import PlaceCoworking, UsersCoworking
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
    
def show_place_view(request: WSGIRequest, place_id):
    try:
        place = PlaceCoworking.objects.get(id=place_id)  # Получение только ОДНОЙ записи.

    except PlaceCoworking.DoesNotExist:
        # Если не найдено такой записи.
        raise Http404
        
    return render(request, "coworking-place.html", {"place": place})
