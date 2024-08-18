from django.contrib import admin

from .models import *
from .models import User

# Register your models here.


admin.site.register(Projet)
admin.site.register(Rapport)
admin.site.register(Perdieme)
admin.site.register(Materiel)
admin.site.register(Personnel)
admin.site.register(PerdiemeValidation)
admin.site.register(Typemateriel)

