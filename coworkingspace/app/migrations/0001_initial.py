# Generated by Django 5.0.4 on 2024-04-22 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('requirement', models.TextField(verbose_name='Требования')),
                ('meeting_time', models.DateField(verbose_name='Дата')),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_cooworking', to='app.placecoworking', verbose_name='Номер место ковореинга')),
            ],
            options={
                'db_table': 'users_coworking',
                'ordering': ['-meeting_time'],
            },
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('coworking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.userscoworking')),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_review',
                'ordering': ['created_at'],
            },
        ),
    ]
