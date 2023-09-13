from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profil
     

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ResetForm(forms.Form):
    email = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={ 'class':'form-control mb-4'}))

class ChangePwdForm(forms.Form):
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'mb-4 form-control'}))
    pwd_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'mb-4 form-control'}))
    

all_contries  = [(93, "Afghanistan"), (355, "Albanie"), (213, "Algérie"), (376, "Andorre"), (244, "Angola"), (1264, "Anguilla"), (672, "Antarctique"), (1268, "Antigua-et-Barbuda"), (54, "Argentine"), (374, "Arménie"), (297, "Aruba"), (61, "Australie"), (43, "Autriche"), (994, "Azerbaïdjan"), (1242, "Bahamas"), (973, "Bahreïn"), (880, "Bangladesh"), (1246, "Barbade"), (375, "Biélorussie"), (32, "Belgique"), (501, "Belize"), (229, "Bénin"), (1441, "Bermudes"), (975, "Bhoutan"), (591, "Bolivie"), (599, "Bonaire, Saint-Eustache et Saba"), (387, "Bosnie-Herzégovine"), (267, "Botswana"), (55, "Brésil"), (246, "Territoire britannique de l'océan Indien"), (1284, "Îles Vierges britanniques"), (673, "Brunei"), (359, "Bulgarie"), (226, "Burkina Faso"), (257, "Burundi"), (855, "Cambodge"), (237, "Cameroun"), (1, "Canada"), (238, "Cap-Vert"), (1345, "Îles Caïmans"), (236, "République centrafricaine"), (235, "Tchad"), (56, "Chili"), (86, "Chine"), (61, "Île Christmas"), (357, "Chypre"), (61, "Îles Cocos (Keeling)"), (57, "Colombie"), (269, "Comores"), (242, "Congo"), (243, "République démocratique du Congo"), (682, "Îles Cook"), (506, "Costa Rica"), (385, "Croatie"), (53, "Cuba"), (599, "Curaçao"), (357, "Chypre"), (420, "République tchèque"), (45, "Danemark"), (253, "Djibouti"), (1767, "Dominique"), (1809, "République dominicaine"), (1829, "République dominicaine"), (1849, "République dominicaine"), (593, "Équateur"), (20, "Égypte"), (503, "Salvador"), (240, "Guinée équatoriale"), (291, "Érythrée"), (372, "Estonie"), (251, "Éthiopie"), (500, "Géorgie du Sud-et-les Îles Sandwich du Sud"), (298, "Îles Féroé"), (679, "Fidji"), (358, "Finlande"), (33, "France"), (689, "Polynésie française"), (241, "Gabon"), (220, "Gambie"), (995, "Géorgie"), (49, "Allemagne"), (233, "Ghana"), (350, "Gibraltar"), (30, "Grèce"), (299, "Groenland"), (1473, "Grenade"), (590, "Guadeloupe"), (1671, "Guam"), (502, "Guatemala"), (44, "Royaume-Uni"), (224, "Guinée"), (245, "Guinée-Bissau"), (592, "Guyana"), (509, "Haïti"), (504, "Honduras"), (852, "Hong Kong"), (36, "Hongrie"), (354, "Islande"), (91, "Inde"), (62, "Indonésie"), (98, "Iran"), (964, "Irak"), (353, "Irlande"), (972, "Israël"), (39, "Italie"), (1876, "Jamaïque"), (81, "Japon"), (962, "Jordanie"), (7, "Kazakhstan"), (254, "Kenya"), (686, "Kiribati"), (383, "Kosovo"), (965, "Koweït"), (996, "Kirghizistan"), (856, "Laos"), (371, "Lettonie"), (961, "Liban"), (266, "Lesotho"), (231, "Libéria"), (218, "Libye"), (423, "Liechtenstein"), (370, "Lituanie"), (352, "Luxembourg"), (853, "Macao"), (389, "Macédoine du Nord"), (261, "Madagascar"), (265, "Malawi"), (60, "Malaisie"), (960, "Maldives"), (223, "Mali"), (356, "Malte"), (692, "Îles Marshall"), (596, "Martinique"), (222, "Mauritanie"), (230, "Maurice"), (262, "La Réunion"), (52, "Mexique"), (691, "Micronésie"), (373, "Moldavie"), (377, "Monaco"), (976, "Mongolie"), (382, "Monténégro"), (1664, "Montserrat"), (212, "Maroc"), (258, "Mozambique"), (95, "Myanmar"), (264, "Namibie"), (674, "Nauru"), (977, "Népal"), (31, "Pays-Bas"), (687, "Nouvelle-Calédonie"), (64, "Nouvelle-Zélande"), (505, "Nicaragua"), (227, "Niger"), (234, "Nigeria"), (683, "Niue"), (672, "Île Norfolk"), (850, "Corée du Nord"), (1670, "Îles Mariannes du Nord"), (47, "Norvège"), (968, "Oman"), (92, "Pakistan"), (680, "Palaos"), (507, "Panama"), (675, "Papouasie-Nouvelle-Guinée"), (595, "Paraguay"), (51, "Pérou"), (63, "Philippines"), (64, "Îles Pitcairn"), (48, "Pologne"), (351, "Portugal"), (1787, "Porto Rico"), (1939, "Porto Rico"), (974, "Qatar"), (262, "Réunion"), (40, "Roumanie"), (7, "Russie"),(250, "Rwanda"), (590, "Saint-Barthélemy"), (290, "Sainte-Hélène"), (1869, "Saint-Kitts-et-Nevis"), (1758, "Sainte-Lucie"), (590, "Saint-Martin"), (508, "Saint-Pierre-et-Miquelon"), (1784, "Saint-Vincent-et-les Grenadines"), (685, "Samoa"), (378, "Saint-Marin"), (239, "Sao Tomé-et-Principe"), (966, "Arabie saoudite"), (221, "Sénégal"), (381, "Serbie"), (248, "Seychelles"), (232, "Sierra Leone"), (65, "Singapour"), (421, "Slovaquie"), (386, "Slovénie"), (677, "Îles Salomon"), (252, "Somalie"), (27, "Afrique du Sud"), (500, "Géorgie du Sud-et-les Îles Sandwich du Sud"), (82, "Corée du Sud"), (211, "Soudan du Sud"), (34, "Espagne"), (94, "Sri Lanka"), (249, "Soudan"), (597, "Suriname"), (47, "Svalbard et Jan Mayen"), (268, "Eswatini"), (46, "Suède"), (41, "Suisse"), (963, "Syrie"), (886, "Taïwan"), (992, "Tadjikistan"), (255, "Tanzanie"), (66, "Thaïlande"), (670, "Timor oriental"), (228, "Togo"), (690, "Tokelau"), (676, "Tonga"), (1868, "Trinité-et-Tobago"), (216, "Tunisie"), (90, "Turquie"), (993, "Turkménistan"), (1649, "Îles Turques-et-Caïques"), (688, "Tuvalu"), (256, "Ouganda"), (380, "Ukraine"), (971, "Émirats arabes unis"), (598, "Uruguay"), (998, "Ouzbékistan"), (678, "Vanuatu"), (379, "Cité du Vatican"), (58, "Venezuela"), (84, "Viêt Nam"), (1284, "Îles Vierges britanniques"), (1340, "Îles Vierges américaines"), (681, "Wallis-et-Futuna"), (212, "Sahara occidental"), (967, "Yémen"), (260, "Zambie"), (263, "Zimbabwe")]

class registerForm(forms.Form):
    lname = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'mb-4 form-control'}))
    fname = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'mb-4 form-control'}))
    cont = forms.ChoiceField(choices=all_contries, widget=forms.Select(attrs={'class':'mb-4 form-control'}))
    number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'mb-4 form-control'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'mb-4 form-control'}))
    pwd_confirm = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput(attrs={'class':'mb-4 form-control'}))
    email = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={'placeholder':'Entrez votre adresse gmail', 'class':'form-control mb-4'}))




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
Sexes = [('M', 'Maxculin'),('F','Féminin'),('indéfini', 'Indéfini')]


class MakeProfilForm(forms.Form):
    photo = forms.ImageField(widget=forms.ClearableFileInput( attrs={'class':'form-control form-control border-0 bg-light rounded-end ps-1'}), required=True)
    sex = forms.CharField(widget=forms.Select(choices=Sexes, attrs={'class':'form-control form-control border-0 bg-light rounded-end ps-1'}))
    desc = forms.CharField(max_length=830, widget=forms.Textarea(attrs={'placeholder':'Votre description','class':'form-control form-control border-0 bg-light rounded-end ps-1'}))



class MkProfil (ModelForm):
    class Meta:
        model = Profil
        fields = ['photo','desc','sex'] 