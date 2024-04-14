from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Наследуем все поля из `AbstractUser`
    данные совпадают с данными из лдап
    переименовыеам таблицу в базе данных
    """
    class Meta:
        db_table = "users"

