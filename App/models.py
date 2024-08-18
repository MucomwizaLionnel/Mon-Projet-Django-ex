from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 
from datetime import datetime;
# 1
class Personnel(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="personnel_user")
    nom_prenom=models.CharField(max_length=100,blank=True, null=True)
    
    date_naissance =models.DateField(default=datetime.now,null=True)
    genre =models.CharField(max_length=100,null=True)
    grade=models.CharField(max_length=100,null=True)
    telephone =models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100, null = True)
    date_enre=models.DateField(default=datetime.now,null=True)


    def __str__(self):
        return self.nom_prenom if self.nom_prenom else "Nom non spécifié"


#2
class Projet(models.Model):
    nom_projet=models.CharField(max_length=100,null=True)
    chef_projet=models.ForeignKey(Personnel,on_delete=models.CASCADE,null=True)
    lieu=models.CharField(max_length=100,null=True)
    date_debut=models.DateField(null=True)
    date_fin=models.DateField()
    description_projet=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nom_projet if self.nom_projet else "Nom non spécifié"
# 3
class Rapport(models.Model):
    personnel=models.ForeignKey(Personnel,on_delete=models.CASCADE,null=True)
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE,null=True)
    titre_rapport=models.CharField(max_length=150,null=True)
    description_file = models.FileField(upload_to='documents/', null=True)
    date=models.DateField()
    
    def __str__(self):
        return self.titre_rapport if self.titre_rapport else "Nom non spécifié"
# 4
class Typemateriel(models.Model):
    nom_type_materel=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.nom_type_materel if self.nom_type_materel else "Nom non spécifié"
class Materiel(models.Model):
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE,null=True) 
    nom_materiel=models.CharField(max_length=100,null=True)
    type_materiel=models.ForeignKey(Typemateriel,on_delete=models.CASCADE,null=True) 
    quantite_materiel=models.CharField(max_length=100,null=True)
    qualite=models.CharField(max_length=100,null=True)
    date_d_enregistrement=models.DateField(null=True) 
       
    def __str__(self) :
        return self.nom_materiel if self.nom_materiel else "Nom non spécifié"   



# 5
class Perdieme(models.Model) :
    personnel=models.ForeignKey(Personnel,on_delete=models.CASCADE,null=True)
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE,null=True)
    description= models.CharField(max_length=100,null=True)
    montant=models.IntegerField()
    date_transaction=models.DateField()
    code_transaction_numero_bordereau=models.CharField(max_length=100,null=True)
 
    def __str__(self):
        return self.description if self.description else "Nom non spécifié"

#6
class PerdiemeValidation(models.Model):
    perdieme = models.ForeignKey(Perdieme, on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    date_validation = models.DateField(auto_now_add=True)
    is_validated = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.personnel} - {self.perdieme}"
    
    
    
    
    
    

    
    