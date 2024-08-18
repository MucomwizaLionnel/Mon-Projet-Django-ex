
from django.urls import path
from .import views 



urlpatterns = [

    path('',views.index ,name="index" ),
    path('login/',views.login_view ,name='login_view' ),
    path('register/',views.register ,name='register' ),
    path('home/',views.home,name='home' ),
   
    path('tablau/',views.tableaubord,name='tableaubord' ),
    # path('chef_equipe/',views.responsables,name='responsables' ),
  
    path('projet/',views.liste_des_projets,name='listedesprojet'),
    path('personnel/',views.liste_des_personnel,name='liste_personnel' ),
    path('Ajouter_personnel/',views.ajouter_personnel,name='AjouterPersonnel' ),
    path('editer_personnel<int:pk>/',views.edit_personnel,name='editerpersonnel'),
    path('supprimer_personn<int:pk>/',views.supprimer_personnel,name='supprimer_les_personnel'),
    path('creer_projet',views.creer_projet,name='creer' ),
    path('editer_projet<int:pk>/',views.edit_projet,name='editer'),
    path('supprimer_projet<int:pk>/',views.supprimer_projet,name='effacer'),
    path('materiel',views.liste_materiel,name='liste_materiel' ),
    path('Ajouter_un_materiel',views.ajouter_materiel,name='ajoutmateriel' ),
    path('editermat<int:pk>/',views.editer_materiel, name='editerMateriel'),
    path('supprimermateriel<int:pk>/',views.supprimer_materiel,name='effacer_materiel'),
    path('print/', views.print_materiel, name='print_materiel'),
    path('perdieme/', views.liste_perdieme, name='listeperdieme'),
    path('Ajoutperdieme/', views.ajouter_perdieme, name='ajouterperdieme'),
    
    path('projet/<int:id>/', views.projet_detail, name='projet_detail'),#le lien qui permer de clique sur les detaill des projet
    path('Validation/<int:id>/', views.validate_perdieme, name='valide'),#le lien de validation de perdieme

    path('listeperdi/', views.perdieme_list, name='listeperdi'), #verification des perdieme valider ou non valider
    # path('actualite/', views.Actualites, name='actualites'),
    path('tableaubordtechnicien/', views.tableaubordtech, name='tableaubordTechn'),


    path('rapport',views.rapport_view,name='rapport' ),
    path('listerapport',views.liste_rapport,name='listerapport'),
    path('tableaubordchefs/',views.tableaubordchef,name='tableauborddeschef'),
    path('touslesprojet/',views.listeprojet,name='touslesprojet')
    
    

    
   
]