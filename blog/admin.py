from django.contrib import admin
from .models import Post #importação da classe (modelo Post) criado em models.py

#para tornar o modelo visível na página de administração (eis a forma de registro)
admin.site.register(Post) 
