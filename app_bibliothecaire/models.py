from django.db import models

class Membres(models.Model):
    name = models.fields.CharField(max_length=150)
    first_name = models.fields.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    creation_date = models.DateTimeField()


class Media(models.Model):
    MEDIA_TYPES = [
        ('livre', 'Livres'),
        ('dvd', 'DVD'),
        ('cd', 'CD'),
        ('jeu_plateau', 'Jeu Plateau'),
    ]
    name_media = models.fields.CharField(max_length=150)
    auteur = models.fields.CharField(max_length=150)
    media_type = models.fields.CharField(max_length=50, choices=MEDIA_TYPES)
    disponible = models.BooleanField(default=True)


class Emprunt(models.Model):
    name_media = models.fields.CharField(max_length=150)
    dateEmprunt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    name_emprunteur = models.fields.CharField(max_length=150)

