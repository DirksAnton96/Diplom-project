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
    users = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,related_name="users_cooworking",verbose_name="Пользователи")
    places = models.ForeignKey(PlaceCoworking, on_delete=models.CASCADE,related_name="users_cooworking",verbose_name="Номер место ковореинга")
    
    requirement = models.TextField(verbose_name='Требования')
    #meeting_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    meeting_time = models.DateField(verbose_name='Дата')
    
    class Meta:
        db_table = "users_coworking"
        ordering = ['-meeting_time']
        indexes = [
            models.Index(fields=("meeting_time",), name="meeting_time_index")
        ]
        unique_together = ["users", "places", "meeting_time"]


class UserReview(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,related_name="user_reviews",verbose_name="Пользователи")
    coworking = models.OneToOneField(UsersCoworking, on_delete = models.CASCADE, primary_key = True)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "user_review"
        ordering = ['created_at']
        indexes = [
            models.Index(fields=("created_at",), name="created_at_index")
        ]
        

    