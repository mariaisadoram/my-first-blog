from django.shortcuts import render
#importing to show the real posts thats were published
from django.utils import timezone
#display this model
from .models import Post

def post_list(request): 
    #shows actual publications sorted by publication date
    #'post' is a variable to QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})