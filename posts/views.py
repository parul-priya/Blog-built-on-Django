from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request) :
	posts = Post.objects.order_by('-pub_date')

	return render(request, 'posts/home.html', {'posts' : posts})

def about(request) :

	return render(request, 'posts/about.html')

def contact(request) :

	return render(request, 'posts/contact.html')


def posts_detail(request, posts_id) :
	post = Post.objects.get(pk=posts_id)
	return render(request, 'posts/posts_detail.html', {'post' : post})