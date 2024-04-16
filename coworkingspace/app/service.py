import os, pathlib
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet, Q, F
from django.conf import settings
from django.contrib.postgres.aggregates import ArrayAgg

from .models import User, PlaceCoworking, UsersCoworking

def queryset_optimization(queryset: QuerySet[UsersCoworking]) -> QuerySet[UsersCoworking]:
    return (
        queryset  # Запрос
        .select_related("users")  # Вытягивание связанных данных из таблицы Users в один запрос
        .prefetch_related("places")  # Вытягивание связанных данных из таблицы Places в отдельные запросы
        .annotate(
            # Создание нового вычисляемого поля username из связанной таблицы User
            username=F('user__username'),

            # Создание массива для место коворкинга  для каждой заявки
            place_names=ArrayAgg('place__names', distinct=True)
        )
        .values("id", "title", "created_at", "username","place_names")  # Выбор только указанных полей для результата
        .distinct()  # Убирание дубликатов, если они есть
        .order_by("-created_at")  # Сортировка результатов по убыванию по полю created_at
    )