import os, pathlib
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet, Q, F
from django.conf import settings
from django.contrib.postgres.aggregates import ArrayAgg

from .models import PlaceCoworking, UsersCoworking
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
        .values("meeting_time", "username","place_names")  # Выбор только указанных полей для результата
        .order_by("meeting_time")
        #.distinct()  # Убирание дубликатов, если они есть
        #.order_by("-created_at")  # Сортировка результатов по убыванию по полю created_at
    )