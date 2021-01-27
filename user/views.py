from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import registerForm
from blogs.models import Post
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def register(request):

	if request.method == 'POST':
		form = registerForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:index'))
	else:
		form = registerForm()

	return render(request,'user/register.html',{'form':form})

class profile(LoginRequiredMixin,View):

	login_url = '/blogs/login/'

	redirect_field_name='blogs:login'

	template_name = 'user/profile.html'

	
	def get(self,request,*args,**kwargs):
		
		context = {

				'posts':Post.objects.filter(user=request.user)

		}
		return render(request,self.template_name,context)

