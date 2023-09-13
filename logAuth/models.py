from django.db import models
from django.contrib import admin

# Create your models here.
Sexes = [('M', 'Maxculin'),('F','Féminin'),('indéfini', 'Indéfini')]
Centres_i = [
    ('sport', 'Sport'),
    ('commerce', 'Ventes'),
    ('vues', 'je veux des vues'),
    ('con', 'Nouveaux contacts'),
    ('iphone', 'Iphone'),
    ('sex', 'moins de  18ans'),
    ('cuisine', 'Cuisine'),
    ('photographie', 'Photographie'),
    ('mode', 'Mode'),
    ('jeux vidéo', 'Jeux vidéo'),
    ('technologie', 'Technologie'),
    ('form', 'Formations'),
    ('bdj', 'Blagues'),
    ('danse', 'Danse'),
    ('nature', 'Nature'),
    ('politique', 'Politique'),
    ('histoire', 'Histoire'),
    ('sciences', 'Sciences'),
    ('animaux', 'Animaux'),
    ('cuisine', 'Cuisine'),
    ('csi', 'Hacking'),
    ('bricolage', 'Bricolage'),
    ('musées', 'Musées'),
    ('théâtre', 'Théâtre'),
    ('activités de plein air', 'Activités de plein air'),
    ('philosophie', 'Philosophie'),
    ('lecture', 'Lecture'),
    ('psychologie', 'Psychologie'),
    ('musique classique', 'Musique classique'),
    ('bd et comics', 'BD et Comics'),
    ('astrologie', 'Astrologie'),
    ('décoration', 'Décoration'),
    ('voyages culinaires', 'Voyages culinaires'),
    ('spiritualité', 'Spiritualité'),
    ('yoga', 'Yoga'),
    ('motivine', 'Motivation'),
    ('esports', 'Esports'),
    ('science-fiction', 'Science-fiction'),
    ('beauté', 'Beauté'),
    ('langues étrangères', 'Langues étrangères'),
    ('musique électronique', 'Musique électronique'),
]
class Profil(models.Model):
    name = models.CharField(max_length=40, default='')
    lname = models.CharField(max_length=40, default='')
    email = models.EmailField(max_length=40, default='')
    fname = models.CharField(max_length=40, default='')
    desc = models.TextField(max_length=800, default="Salut, j'utilise WatAdd...")
    photo = models.FileField(upload_to='photos')
    abonnes = models.IntegerField(default=0)
    ajoutes = models.IntegerField(default=0)
    sex = models.CharField(max_length=15, default="", choices=Sexes)
    ind = models.CharField(max_length=5)
    num = models.CharField(max_length=15)
    pref = models.CharField('self', max_length=800, default="", choices=Centres_i)
    added = models.CharField(default="", max_length=17000000000)
    shared = models.IntegerField(default=0)
    payment = models.IntegerField(default=0)
    possible = models.IntegerField(default=20)

class stc(admin.ModelAdmin):
    list_display = ('name','lname','fname', 'email', 'desc','sex','ind', 'photo', 'num', 'added', 'ajoutes', 'abonnes',  'possible', 'shared', 'payment')