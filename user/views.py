from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import registerForm

# Create your views here.

def register(request):

	if request.method == 'POST':
		form = registerForm(request.POST)
		print('here')
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:index'))
	else:
		form = registerForm()

	return render(request,'user/register.html',{'form':form})