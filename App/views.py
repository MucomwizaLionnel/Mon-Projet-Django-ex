from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# from .forms import ProfileForm,LoginForm,FormTache
from django.contrib.auth import authenticate,login
from .models import *

from .forms import *


def index(request):
    return render(request, 'index.html')

def register(request):
    profil_form=ProfileForm(request.POST or None, request.FILES)
    if (request.method=='POST'):
        if (profil_form.is_valid()):
            nom_utilisateur=profil_form.cleaned_data['nom_utilisateur']
            mots_de_pass=profil_form.cleaned_data['mots_de_pass']
            mots_de_pass1=profil_form.cleaned_data['mots_de_pass1']
            nom_prenom=profil_form.cleaned_data['nom_prenom']
            
            date_naissance=profil_form.cleaned_data['date_naissance']
            genre=profil_form.cleaned_data['genre']
            grade=profil_form.cleaned_data['grade']
            telephone=profil_form.cleaned_data['telephone']
            address=profil_form.cleaned_data['address']
            date_enre=profil_form.cleaned_data['date_enre']
            if (mots_de_pass==mots_de_pass1):
                user=User.objects.create_user(username=nom_utilisateur, password=mots_de_pass)

                user.first_name=nom_prenom
                user.last_name=nom_prenom
                
                user.save()
                group = Group.objects.get_or_create(name= "Technicien")
                user.groups.add(group[0])
                profil=Personnel(
                        user=user,
                        nom_prenom=nom_prenom,
                        
						date_naissance=date_naissance,
						genre=genre,
                        grade=grade,
						address=address,
						telephone=telephone,
                        date_enre=date_enre).save()
                if user:
                    login(request, user)
                    return redirect(index)
                else:
                    return redirect(login_view)
            else: 
                profil_form=ProfileForm(request.FILES)
                return render(request, 'register.html',locals())
    return render(request, 'register.html',locals())
    

def login_view(request):
    Connexion_form=ConnexionForm(request.POST or None)
    msg=None
    if request.method=='POST':
        if Connexion_form.is_valid():
            nom_utilisateur=Connexion_form.cleaned_data.get('nom_utilisateur')
            mots_de_pass=Connexion_form.cleaned_data.get('mots_de_pass')
            user=authenticate(username=nom_utilisateur,password=mots_de_pass)


            if user:#si l'objet existe 


                login(request, user)
                groups = [group.name for group in user.groups.all()]
                # if user.is_superuser or 'personnel' in groups:
                #      return redirect(index) #on connecte l'utilisateur
                if user.is_superuser or 'Chef' in groups:
                    return redirect(tableaubordchef) #on connecte l'utilisateur
                if 'Responsable' in groups:
                    return redirect(tableaubord) #on connecte l'utilisateur
                if 'Technicien' in groups:
                    return redirect(tableaubordtech) #on connecte l'utilisateur
                
            
            else:
                Connexion_form=ConnexionForm()
        else:
            Connexion_form=ConnexionForm()
            return render(request, 'login.html', locals())
    return render(request, 'login.html', locals())
        
def home(request):
    return render(request,'index.html')
def liste_des_personnel(request):
    personnels=Personnel.objects.all()
    return render(request,'liste_personnel.html',{'personnels': personnels})  
def ajouter_personnel(request):
    if request.method=='POST':
        form=Personnel_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('liste_personnel')    
    else:
        form=Personnel_form()
    return render(request,'personnel_form.html',{'form':form})      
def edit_personnel(request,pk):
    personnels=get_object_or_404(Personnel,pk=pk)
    if request.method=='POST':
        form=Personnel_form(request.POST,instance=personnels)
        if form.is_valid():
            form.save()
            return redirect('liste_personnel')
    else:
        form=Personnel_form(instance=personnels)

    return render(request,'personnel_form.html',{'form':form})
   
def supprimer_personnel(request,pk):
    personnels=get_object_or_404(Personnel,pk=pk)
    if request.method=='POST':
        personnels.delete()
        return redirect('liste_personnel')
    return render(request,'supprimer_personnel.html',{'personnels':personnels})


def liste_des_projets(request):
    projets=Projet.objects.all()
    return render(request,'projet.html',{'projets': projets})
def creer_projet(request):
    if request.method=='POST':
        form=Projet_form(request.POST)
        if form.is_valid():
            form.save() 
           
            
        return redirect('listedesprojet')
    else:
        form=Projet_form()

    return render(request,'projet_form.html',{'form':form})    

def edit_projet(request,pk):
    projets=get_object_or_404(Projet,pk=pk)
    if request.method=='POST':
        form=Projet_form(request.POST,instance=projets)
        if form.is_valid():
            form.save()
            return redirect('listedesprojet')
    else:
        form=Projet_form(instance=projets)

    return render(request,'projet_form.html',{'form':form})

def supprimer_projet(request,pk):
    projets=get_object_or_404(Projet,pk=pk)
    if request.method=='POST':
        projets.delete()
        return redirect('listedesprojet')
    return render(request, 'supprimer_projet.html', {'projets': projets})
def liste_materiel(request):
    materiels=Materiel.objects.all()
    return render(request,'materiel.html',{'materiels':materiels})

def ajouter_materiel(request):
    if request.method=='POST':
        form=Materiel_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_materiel')
    else:
        form=Materiel_form()

    return render(request,'materiel_form.html',{'form':form})    

def editer_materiel(request,pk):
    materiels=get_object_or_404(Materiel,pk=pk)
    if request.method=='POST':
        form=Materiel_form(request.POST,instance=materiels)
        if form.is_valid():
            form.save()
            return redirect('liste_materiel')
    else:
        form=Materiel_form(instance=materiels)

    return render(request,'materiel_form.html',{'form':form})   

def supprimer_materiel(request,pk):
    materiels=get_object_or_404(Materiel,pk=pk)
    if request.method=='POST':
        materiels.delete()
        return redirect('liste_materiel')
    return render(request, 'supprimer_mat.html', {'materiels':materiels})
def liste_perdieme(request):
   
    perdiemes=Perdieme.objects.all()
    return render(request,'perdieme.html',{'perdiemes':perdiemes})
def ajouter_perdieme(request):
    if request.method=='POST':
        form=Perdieme_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listeperdieme')
    else:
        form=Perdieme_Form()

    return render(request,'perdieme_form.html',{'form':form})        


def tableaubord(request):
      

     return render(request,'tableaubord.html')
 
def responsables(request):
    return render(request,'chef_equipe.html')    
# def liste_personnel(request):
#     personnels = Personnel.objects.all()
#     return render(request, 'liste_personnel.html', {'personnels': personnels})
    
def transaction(request):
    return render(request,'transaction.html') 
def charge(request):
    return render(request,'charge.html') 

def liste_rapport(request):
    rapports=Rapport.objects.all()
    return render(request,'liste_rapport.html',{'rapports':rapports})    

def rapport_view(request):
    if request.method == 'POST':
        
        form =Rapport_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rapport')  # Redirigez vers une page de succès ou une autre vue
    else:
        form = Rapport_Form()
    
    context = {
        'form': form,
    }
    return render(request, 'rapport.html', context)


def rapport(request):
    return render(request,'rapport.html') 



def navigation(request):
    return render(request,'nav.html')
def print_materiel(request):
    materiels = Materiel.objects.all()
    return render(request, 'print.html', {'materiels': materiels})


def listeprojet(request):
    projets = Projet.objects.all()
    return render(request, 'touslesprojet.html', {'projets': projets})
def projet_detail(request, id):
    projet = get_object_or_404(Projet, id=id)
    personnels = Personnel.objects.filter(projet=projet)
    rapports = Rapport.objects.filter(projet=projet)
    materiels = Materiel.objects.filter(projet=projet)
    perdiems = Perdieme.objects.filter(projet=projet)

    context = {
        'projet': projet,
        'personnels': personnels,
        'rapports': rapports,
        'materiels': materiels,
        'perdiems': perdiems,
    }
    return render(request, 'projet_detail.html', context)


def validate_perdieme(request, id):
    perdieme = get_object_or_404(Perdieme, id=id)
    
    # Utiliser le related_name défini dans le modèle Personnel
    personnel = request.user.personnel_user  # Accéder à l'objet Personnel lié

    # Vérifiez si le personnel de la requête correspond au personnel du per diem
    if perdieme.personnel != personnel:
        # Redirigez vers une page d'erreur ou affichez un message d'erreur
        return redirect('error_page')  # Changez ceci en l'URL de votre choix

    validation, created = PerdiemeValidation.objects.get_or_create(perdieme=perdieme, personnel=personnel)

    if request.method == 'POST':
        form = PerdiemeValidationForm(request.POST, instance=validation)
        if form.is_valid():
            form.save()
            return redirect('listeperdi')  # Changez ceci en l'URL de votre choix
    else:
        form = PerdiemeValidationForm(instance=validation)

    return render(request, 'validate_perdieme.html', {'form': form, 'perdieme': perdieme})

    class Meta:
        model = PerdiemeValidation
        fields = ['is_validated']
        labels = {
            'is_validated': 'Validation',
        }
        widgets = {
            'is_validated': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        
        
def perdieme_list(request):
    # Récupérer tous les objets Perdieme
    perdiemes = Perdieme.objects.all()
    
    # Préparer les données pour le template
    perdieme_data = []
    for perdieme in perdiemes:
        validations = PerdiemeValidation.objects.filter(perdieme=perdieme)
        is_validated = any(validation.is_validated for validation in validations)
        perdieme_data.append({
            'perdieme': perdieme,
            'is_validated': is_validated,
        })
    
    context = {
        'perdieme_data': perdieme_data,
    }
    
    return render(request, 'perdieme_list.html', context)


def Actualites(request):
    
    render(request, 'actualite.html')
    
def tableaubordchef(request):
    return render(request, 'tableaubordchef.html') 
    
    
def tableaubordtech(request):
    return render(request, 'tableaubordtech.html')
def projetdetail(request):
    return render(request, 'touslesprojet.html')