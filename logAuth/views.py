from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .formulaire import LoginForm, registerForm, MkProfil, ResetForm, ChangePwdForm, MakeProfilForm
from .models import Profil
import requests
from string import ascii_uppercase, digits
from random import choice



# from django.http import JsonResponse
def generate_username(letter, number):
    generated = ""
    generated += choice(number)
    for i in range(4):
        generated += choice(letter)
    return generated
    

# Create your views here.
def login1(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            try:
                emailed = User.objects.get(email=username)
                if emailed:
                    username = emailed.username
            except:
                try:
                    numbered = Profil.objects.get(num=username)
                    if numbered:
                        username = numbered.name
                except:
                    if username[-1] in digits:
                        mess = "Numero non enregistré !"
                    else:
                        mess = "Adresse gmail non inscrit !"
                    messages.error(request, mess)
                    return render(request, "login.html", {'form':form})
            pwd = request.POST['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                # return (request)
                # users = Profil.objects.all()
                return redirect(f"dashboard/{username}/all")
            # messages.error(request, "Invalid Creantials !")
            # return render(request, "login.html", {'form':form})
        else:
            # for fields in form.errors:
                # form[fields].field.widget.attrs['class'] += 'bg-danger'
            messages.error(request, "Invalid Creantials !")
            return render(request, "login.html", {'form':form})
    else:
        form = LoginForm()
        return render(request, "login.html", {'form':form})

def register1(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            pwd = request.POST['pwd']
            email = request.POST['email']
            lname = request.POST['lname']
            fname = request.POST['fname']
            email = request.POST['email']
            c_pwd = request.POST['pwd_confirm']
            number = '+' +  request.POST['cont'] + request.POST['number']
            numb = '+' +  request.POST['cont'] + request.POST['number']
            ind =  '00' + request.POST['cont']
            email = request.POST['email']
            ready =  User.objects.all()
            used = True
            username = generate_username(ascii_uppercase, digits)
            while used:
                for u in ready:
                    if u.username == username:
                        username = generate_username(ascii_uppercase, digits)
                    else:
                        used = False
            try:
                deja = User.objects.get(email=email)
                if deja:
                    messages.error(request, "Adresse mail déja utilisé !! ")
                    form = registerForm()
                    return render(request, "register.html", {'form':form})
            except:
                pass

            try:
                d = Profil.objects.get(num=numb)  
                if d:
                    messages.error(request, "Numéro déja utilisé !!! ")
                    form = registerForm()
                    return render(request, "register.html", {'form':form})
            except:
                pass
            if pwd != c_pwd:
                messages.error(request, "Différents mots de passe !")
                form = registerForm()
                return render(request, "register.html", {'form':form})
    
            if request.POST['number'][0] == "0" or request.POST['number'][0] == "+":
                messages.error(request, "Choisissez le pays et ne mettez l'indicatif avant le numéro")
                form = registerForm()
                return render(request, "register.html", {'form':form}) 
            user = User.objects.create_user(username=username, password=pwd, email=email, last_name=lname, first_name=fname)
            if user is not None:
                user.save()
                new_profil = Profil(name=username, fname=fname, lname=lname, email=email, ind=ind, num =numb)
                new_profil.save()
                user = authenticate(username=username, password=pwd)
                if user is not None:
                    login(request, user)
                    return redirect(f"/dashboard/{username}/all")
                return redirect("login-add")
        for fields in form.errors:
            form[fields].field.widget.attrs['class'] += 'is-invalid'
        messages.error(request, "Entrées Invalides !")
    form = registerForm()
    return render(request, "register.html", {'form':form})

def PrefChoice(request):
    if request.user.is_authenticated:
        online = request.user.username
    else:
        return redirect("/log")
    preference = {'Data science': 'DataScience', 'Développement mobile': 'mobile', 'Programmation': 'programing', 'Optimisation SEO': 'seo', 'Développement Web': 'webbing', 'Graphisme': 'desing', 'Sales plans🔞': 'dirty', 'Vues': 'visibility', 'Maintenace informatique': 'maininfo', 'Marketing': 'marketing', "Ventes d'accessoires": 'accessory', 'Ventes et Achats de vêtements': 'clothes', 'Accessoires beauté': 'beauty', 'Musique': 'music', 'Immobilier': 'immobilier', 'Marché Digital': 'digitmarket', 'Coaching': 'coach', 'Maths et logique': 'scientist', 'Nouveaux Contacts': 'newcontact'}
    prefs = ["DataScience", "mobile", "programing", "seo", "webbing",  "desing", "dirty", "visibility", "maininfo", "marketing", "accessory", "clothes", "beauty", "music", "immobilier", "digitmarket", "coach",  "scientist", "newcontact"]
    noms = ['Data science', 'Développement mobile', 'Programmation', 'Optimisation SEO', 'Développement Web', 'Graphisme', 'Sales plans🔞', 'Vues', 'Maintenace informatique', 'Marketing', "Ventes d'accessoires", 'Ventes et Achats de vêtements', 'Accessoires beauté', 'Musique', 'Immobilier', 'Marché Digital', 'Coaching', 'Maths et logique', 'Nouveaux Contacts']
    prof = Profil.objects.get(name=online)
    if request.method == "POST":
        for name, value in request.POST.items():
                   print()
                   if name.startswith('pref_'):
                        choiced = name.replace('pref_', '')
                        choiced = preference[choiced]
                        if choiced not in prof.pref.split():
                            prof.pref += choiced+' '
                        print(choiced)
                        prof.save()
    for elt in noms:
            for x in prof.pref.split():
                if preference[elt] == x:
                    print(True)
                    noms.remove(elt)
    return render(request, "prefers.html", {'profil':prof, 'prefs':noms})
    
                       

def logout1(request):
    logout(request)
    print("uuuuu")
    return redirect("login-add")

def profilize(request, online):
    if request.method == "POST":
        form = MakeProfilForm(request.POST, request.FILES )
        profil = Profil.objects.get(name=online)
        profil.desc = request.POST['desc']
        profil.sex = request.POST['sex']
        profil.photo = request.FILES['photo']
        profil.save()
        return redirect("home")
    form = MakeProfilForm()
    return render(request, "modifProfil.html", {'form':form})


def add(request, profil, online):
    profab = Profil.objects.get(name=profil)
    profab.abonnes += 1
    profab.save()
    profad = Profil.objects.get(name=online)
    profad.ajoutes += 1
    profad.added += ' '+ profil
    profad.save()
    link = f'https://api.whatsapp.com/send?phone={profab.num}&text=Hello%21%20.%20Je%20vous%20ai%20vu%20sur%20WatAdd%OA%OAJe%20Je%20suis{profad.name}%OA{profad.desc}'
    return redirect(f"/dashboard/{online}/all")
    
def index(request):
    return render(request, "index.html")

def categorise(s, category):
    if not s:
        all_profil = Profil.objects.all()
        tried = []
        for elt in all_profil:
            if category in elt.pref:
                tried += elt
    else:
        all_profil = Profil.objects.all()
        tried = []
        for elte in all_profil:
            if s in elte.fname or s in elte.lname:
                tried += elte
    return tried

def dashboard(request, profil, category):
    liste = []
    if request.user.is_authenticated:
        profil = request.user.username
    else:
        return redirect("/log")
    subject = ''
    if request.method == "POST":
        subject = request.POST['subject']
    profil = Profil.objects.get(name=profil)
    others = Profil.objects.all()
    print(type(others))
    if category != "all" or not subject:
        others = categorise(subject, category)
    for elt in others:
        if elt.name == profil.name:
            pass
        else:
            liste.append(elt)
    for elte in liste:
        if elte.name in profil.added:
            liste.remove(elte)
    liste.sort(key=lambda e: (e.ajoutes, e.ind==profil.ind), reverse=True)
    print(liste)
    return render(request, "dashboard.html",  {'profil':profil,'subject':subject, 'others':liste})

def reset(request):
    form = ResetForm()
    sent =""
    if request.method == "POST":
        form = ResetForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            try:
                emailed = User.objects.get(email=email)
                if emailed:
                    sent = "sent"
                    return render(request, "reset_password.html",  {'status':sent})
            except:
                messages.error(request, "Adresse email non enrégistrée !")
                return render(request, "reset_password.html",  {'status':sent, 'form':form })   
        else:
            form = ResetForm()
            sent =""
            messages.error(request, "Entrée invalide !")
            return render(request, "reset_password.html",  {'status':sent, 'form':form })
    return render(request, "reset_password.html",  {'status':sent, 'form':form })

def changePwd(request, email):
    form = ChangePwdForm()
    online = User.objects.get(email=email)
    reseted = ""
    if request.method == "POST":
        form = ChangePwdForm(request.POST)
        if form.is_valid():
            password = request.POST['pwd']
            password_confirm = request.POST['pwd_confirm']
            if password_confirm != password:
                messages.error(request, "Différents mots de passe !")
                form = ChangePwdFormForm()
                return render(request, "change.html", {'form':form, 'reseted':reseted})
            else:
                online.password = password
                online.save()
                reseted = "Votre mot de passe a été bien réinitialisé ✅ "
                return render(request, "change.html", {'form':form, 'reseted':reseted})
    return render(request, "change.html", {'form':form, 'reseted':reseted})
    






    



def share(request, online):
    linkAD = ''
    prof = Profil.objects.get(name=online)
    prof.possible += 5
    prof.shared += 1
    prof.save()
    link = f'https://api.whatsapp.com/send?&text=Hello%21%20.%20Rejoins%20nous%20pour%20enregistrer%20plus%20de%20contacts%20sur%20WatAdd%OA{linkAD}'
    return redirect("home")

def payment(request, online):
    if request.method == "POST":
        prof = Profil.objects.get(name=online)
        montant = 200
        dest = '22997776684'
        if '+' in dest or dest.index('00') == 0:
            return redirect("pay")
        try:
            int(dest)
        except:
            return redirect("pay")
        dep = request.POST['dep']
        # Informations d'authentification (à remplacer par vos clés d'authentification)
        developer_id = 'VOTRE_DEVELOPER_ID'
        api_user = 'VOTRE_API_USER'
        api_key = 'VOTRE_API_KEY'

        # Construire l'URL de l'API MTN MoMo
        base_url = 'https://api.momoapi.mtn.com'
        transaction_endpoint = '/v1_0/transfer'
        api_url = f'{base_url}{transaction_endpoint}'

        # Construire l'en-tête d'authentification
        headers = {
            'Authorization': f'Basic {api_user}:{api_key}',
            'X-Reference-Id': 'UN_IDENTIFIANT_UNIQUE_POUR_VOTRE_TRANSACTION',
            'Content-Type': 'application/json',
        }

        # Construire le corps de la requête
        payload = {
            'amount': montant,
            'currency': 'EUR',  # Remplacez par la devise appropriée
            'externalId': 'UN_IDENTIFIANT_EXTERNE_POUR_VOTRE_TRANSACTION',
            'payee': {
                'partyIdType': 'msisdn',
                'partyId': dest,
            }
        }
        # Effectuer la requête POST à l'API MTN MoMo
        response = requests.post(api_url, json=payload, headers=headers)
        # Traiter la réponse
        if response.status_code == 200:
            # La transaction a réussi
            return JsonResponse({'status': 'success', 'message': 'Transaction successful.'})
        else:
            # La transaction a échoué
            error_message = response.json().get('message', 'Unknown error occurred.')
            return JsonResponse({'status': 'error', 'message': error_message}, status=response.status_code)

        #return redirect("home")
    prof = Profil.objects.get(name=online)
    return render(request, "payement.html", {'profil':prof})

    






# username = request.POST['username']
        # pwd = request.POST['pwd']
        # user = authenticate(username=username, password=pwd)
        # if user is not None:
        #     return redirect("home")
        # messages.error(request, "Invalid Creantials !")