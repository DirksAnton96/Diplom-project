import os, pathlib
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet, Q, F
from django.conf import settings
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.utils import IntegrityError

from .models import PlaceCoworking, UsersCoworking, UserReview
from users.models import User

def queryset_optimization(queryset: QuerySet[UsersCoworking]) -> QuerySet[UsersCoworking]:
    return (
        queryset  # Запрос
        .select_related("users")  # Вытягивание связанных данных из таблицы Users в один запрос
        .select_related("places")  # Вытягивание связанных данных из таблицы Places в отдельные запросы
        .annotate(
            # Создание нового вычисляемого поля username из связанной таблицы Users
            username=F('users__username'),

            # Создание нового вычисляемого поля place_names из связанной таблицы coworking_place
            place_names=F('places__name')
        )
        .values("meeting_time", "username","place_names","id")  # Выбор только указанных полей для результата
        .order_by("meeting_time")
        #.distinct()  # Убирание дубликатов, если они есть
        #.order_by("-created_at")  # Сортировка результатов по убыванию по полю created_at
    )
    
def create_coworking(request: WSGIRequest) -> UsersCoworking:
    coworking = UsersCoworking.objects.create(
        meeting_time = request.POST["meeting_time"],
        users = request.user,
        places_id = request.POST.get("places"),
        requirement = request.POST["requirement"]
    )
    return coworking

def update_coworking(request: WSGIRequest, coworking: UsersCoworking) -> UsersCoworking:
    
    coworking.meeting_time = request.POST.get("meeting_time")
    coworking.places_id = request.POST.get("places")
    coworking.requirement = request.POST.get("requirement")
    
    coworking.save()
    
    return coworking


def queryset_optimization_review(queryset: QuerySet[UserReview]) -> QuerySet[UserReview]:
    return (
        queryset  # Запрос
        .select_related("user")  # Вытягивание связанных данных из таблицы Users в один запрос
        .select_related("coworking")  # Вытягивание связанных данных из таблицы Users_coworking в отдельные запросы
        .annotate(
            # Создание нового вычисляемого поля username из связанной таблицы Users
            username=F('user__username'),

            # Создание нового вычисляемого поля meeting_time из связанной таблицы users_coworking
            meeting_time=F('coworking__meeting_time')
        )
        .values("review", "username","created_at","coworking_id","meeting_time","id")  # Выбор только указанных полей для результата
        .order_by("created_at")
    )

def create_review(request: WSGIRequest) -> UserReview:
    review = UserReview.objects.create(
        user = request.user,
        coworking_id = request.POST.get("coworking"),
        review = request.POST["review"]
    )
    return review


def update_review(request: WSGIRequest, review: UserReview) -> UserReview:
    
    review.coworking_id = request.POST.get("coworking")
    review.requirement = request.POST.get("review")
    
    review.save()
    
    return review