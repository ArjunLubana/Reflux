from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MessageForm
from django.core.mail import send_mail

def home(request):

	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid:
			email = request.POST.get('email')
			subject = request.POST.get('subject')
			message = request.POST.get('message')

			send_mail(subject, message, email,['admin@site1.com'])

			return HttpResponseRedirect('/?submitted')
	else:
		form = MessageForm()

	return render(request,'index.html',{'form':form})
