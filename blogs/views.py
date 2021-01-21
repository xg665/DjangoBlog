from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render, reverse
from .models import Post
# Create your views here.
def index(request):
	
	return HttpResponseRedirect(reverse('blogs:leetcode'))
	# return render(request, 'blogs/index.html',{'posts':posts})
def leetcode(request):

	latest_question_list = Post.objects.all()

	print(latest_question_list)

	return render(request, 'blogs/leetcode.html',{'latest_question_list':latest_question_list})

def post(request):

	title = request.POST['title']

	content = request.POST['content']

	category = 'lc'

	url = request.POST['url']

	p = Post(title=title,content=content,category=category,url=url)

	p.save()

	return HttpResponseRedirect(reverse('blogs:leetcode'))


