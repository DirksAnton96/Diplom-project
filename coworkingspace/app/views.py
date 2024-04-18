from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect, Http404,HttpRequest
from django.urls import reverse
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


from .models import PlaceCoworking, UsersCoworking
from .service import queryset_optimization, create_coworking, update_coworking
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
    
    #print(UsersCoworking.objects.filter(users__username=username).query)
    
    return render(request, "users-coworking-list.html", {"usercoworkinslist": queryset})
    
    
    
def show_place_view(request: WSGIRequest, place_id):
    try:
        place = PlaceCoworking.objects.get(id=place_id)  # Получение только ОДНОЙ записи.

    except PlaceCoworking.DoesNotExist:
        # Если не найдено такой записи.
        raise Http404
        
    return render(request, "coworking-place.html", {"place": place})


@login_required
def create_coworkings_view(request: WSGIRequest):
    
    all_place_coworking = PlaceCoworking.objects.all()
    
    if request.method == "POST":
        try:
            coworking = create_coworking(request)
            queryset = queryset_optimization(
                UsersCoworking.objects.filter(users__username=request.user)
            )
        
            return HttpResponseRedirect(reverse('list-users-coworkings', args=[coworking.users]))
        except IntegrityError:
            return render(request, "error.html", {"error": "Бронь на данное число уже существует"})
        except ValidationError:
            return render(request, "error.html", {"error": "Вы не выбрали дату"})
    return render(request, "create_form_coworking.html", {"cw_places": all_place_coworking})

@login_required
def show_coworking_view(request: WSGIRequest, coworking_id):
    try:
        coworking = UsersCoworking.objects.get(id=coworking_id)
    except UsersCoworking.DoesNotExist:
        raise Http404
    return render(request, "show-coworking-request.html", {"coworking": coworking})

@login_required
def update_coworking_view(request: WSGIRequest, coworking_id):
    try:
        all_place_coworking = PlaceCoworking.objects.all()
        coworking = UsersCoworking.objects.get(id=coworking_id)
        
        if coworking.users == request.user:
            if request.method == "POST":
                coworking = update_coworking(request, coworking)
                return HttpResponseRedirect(reverse('list-users-coworkings', args=[coworking.user]))
            else:
                queryset = queryset_optimization(
                    UsersCoworking.objects.filter(users__username=request.user)
                )
                return render(request, "edit_form_coworking.html", {"coworking": coworking, "cw_places": all_place_coworking})
        else:
            return HttpResponseRedirect(reverse('list-users-coworkings', args=[coworking.users]))
             
    except UsersCoworking.DoesNotExist:
        raise Http404


def delete_coworking_view(request: WSGIRequest, coworking_id):
    try: 
        coworking = UsersCoworking.objects.get(id=coworking_id)
        coworking.delete()
        return HttpResponseRedirect(reverse('list-users-coworkings', args=[coworking.users]))
    except UsersCoworking.DoesNotExist:
        raise Http404