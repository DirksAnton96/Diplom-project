# Generated by Django 5.0.4 on 2024-04-14 18:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceCoworking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mode_time', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'db_table': 'coworking_place',
            },
        ),
        migrations.CreateModel(
            name='UsersCoworking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_time', models.DateField(verbose_name='Дата')),
                ('places', models.ManyToManyField(related_name='users_cooworking', to='app.placecoworking', verbose_name='Номер место ковореинга')),
                ('users', models.ManyToManyField(related_name='users_cooworking', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
            options={
                'db_table': 'users_coworking',
                'ordering': ['-meeting_time'],
                'indexes': [models.Index(fields=['meeting_time'], name='meeting_time_index')],
            },
        ),
    ]