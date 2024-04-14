from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class PlaceCoworking(models.Model):
    """
    Сущность рабочего места
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    mode_time = models.DateTimeField(auto_now=True,db_index=True)
    
    class Meta:
        db_table = "coworking_place"

class UsersCoworking(models.Model):
    """
    Сущность бронирования рабочего места
    """        
    users = models.ManyToManyField(get_user_model(),related_name="users_cooworking",verbose_name="Пользователи")
    places = models.ManyToManyField(PlaceCoworking,related_name="users_cooworking",verbose_name="Номер место ковореинга")
    #meeting_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    meeting_time = models.DateField(verbose_name='Дата')
    
    class Meta:
        db_table = "users_coworking"
        ordering = ['-meeting_time']
        indexes = [
            models.Index(fields=("meeting_time",), name="meeting_time_index")
        ]

    