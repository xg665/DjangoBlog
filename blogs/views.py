from django.http import HttpResponse, HttpResponseRedirect
from pathlib import Path
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render, reverse
from .models import Post, Feedback
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import BlogForm
from django.views import View
# Create your views here.
def index(request):
	
	return HttpResponseRedirect(reverse('blogs:leetcode'))
	# return render(request, 'blogs/index.html',{'posts':posts})
def leetcode(request):

	latest_question_list = Post.objects.all()

	print(latest_question_list)

	return render(request, 'blogs/leetcode.html',{'latest_question_list':latest_question_list})


class PostDetail(DetailView):

	model = Post

class PostDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

	login_url = '/blogs/login/'

	redirect_field_name='blogs:login'

	model = Post

	success_url = '/'

	def test_func(self):
		return self.get_object().user==self.request.user

	def get_success_url(self):
	# Assuming there is a ForeignKey from Comment to Post in your model
		post = self.get_object()
		return reverse('blogs:leetcode')

class PostUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):

	login_url = '/blogs/login/'

	redirect_field_name='blogs:login'

	form_class = BlogForm
	
	model = Post

	#fields = ['title','description','code','url']

	def test_func(self):
		
		return self.get_object().user==self.request.user

	def form_valid(self,form):
		
		form.instance.user = self.request.user
		
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
		context['latest_question_list'] = [self.get_object()]
		context['path'] = Path(self.request.path).parent
		return context


class PostCreate(LoginRequiredMixin,CreateView):

	# print(request.path)

	login_url = '/blogs/login/'

	redirect_field_name='blogs:login'

	form_class = BlogForm
	# model = Post

	# fields = ['title','description','content','url']
	
	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
		context['latest_question_list'] = Post.objects.all()
		context['path'] = Path(self.request.path).parent
		return context

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class FeedbackCreate(LoginRequiredMixin,CreateView):

	login_url = '/blogs/login/'

	redirect_field_name='blogs:login'

	model = Feedback

	fields = ['title','description']

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)