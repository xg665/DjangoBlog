from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import registerForm, UserUpdateForm, ProfileUpdateForm
from blogs.models import Post
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):

	if request.method == 'POST':
		form = registerForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)        
			login(request, new_user)
			return HttpResponseRedirect(reverse('blogs:index'))
	else:
		form = registerForm()

	return render(request,'user/register.html',{'form':form})

class profile(View):

	template_name = 'user/profile.html'
	
	def get(self,request,*args,**kwargs):
		# print(self.kwargs['slug'])
		u = User.objects.get(username=self.kwargs['slug'])
		context = {
				'target_user': u,
				'posts':Post.objects.filter(user=u),
		}
		return render(request,self.template_name,context)

@login_required(login_url='/blogs/login/')
def profile_update(request,slug):

	if request.method=='POST':
		
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			
			u_form.save()
			p_form.save()

			return HttpResponseRedirect(reverse('blogs:profile', args=[request.user.username]))
		
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	
	context = {
		'u_form':u_form,
		'p_form':p_form
	}

	return render(request,'user/profileUpdate.html',context)