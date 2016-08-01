from django.shortcuts import render
from blog.models import Post,Category
from django.http import HttpResponse
from blog import models
# Create your views here.
def Post(request, post_id):
	post = models.Post.objects.get(id = post_id)
	context = {
		'post' : post,
	}
	return render(request, 'post.html', context)
	#return HttpResponse('Welcome to my post page' + post_id) 
def Index(request):
	posts = models.Post.objects.all()
	categories = models.Category.objects.all()
	context = {'posts': posts, 'categories': categories}
	return render(request, 'index.html', context)
	#return HttpResponse("Welcom to Index")
def Category(request, category_id):
	category = models.Category.objects.get(id = category_id)
	posts = models.Post.objects.filter(category_id = category_id)
	context = {
	'category': category,
	'posts': posts,
	}
	return render(request, 'category.html', context)