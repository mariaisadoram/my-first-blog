from django.conf import settings
from django.db import models
from django.utils import timezone

#models.Model significa que o Post é um modelo de Django, então o Django sabe que ele 
#deve ser salvo no banco de dados.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #vai unir a outro modelo de django
    title = models.CharField(max_length=200) #para conteudo limitado de caracteres
    text = models.TextField() #para conteudo ilimitado de caracteres
    created_date = models.DateTimeField(default=timezone.now) #data e hora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title