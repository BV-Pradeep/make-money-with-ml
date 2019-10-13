from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
	template_name='register.html'
	if request.method =='POST':
		register_form=RegisterForm(request.POST)
		if register_form.is_valid():
			first_name=register_form.cleaned_data['first_name']
			last_name=register_form.cleaned_data['last_name']
			username=register_form.cleaned_data['username']
			email=register_form.cleaned_data['email']
			password=register_form.cleaned_data['password']
			confirm_password=register_form.cleaned_data['confirm_password']

			if password==confirm_password:
				if User.objects.filter(username=username).exists():
					messages.info(request,'Username Taken!!')
					return redirect('accounts:register')

				elif User.objects.filter(email=email).exists():
					messages.info(request,'Email Taken!!')
					return redirect('accounts:register')

				else:
					user = User.objects.create_user(first_name=first_name,
													last_name=last_name,
													username=username,
													email=email,
													password=password)
					user.save()
					return redirect('accounts:login')

			else:
				messages.info(request,"Password not matching!!")
				return redirect('accounts:register')


	else: 
		register_form=RegisterForm(request.POST)


	context={
				'register_form':register_form,
	}
	return render(request,template_name,context)

def login(request):
	template_name='login.html'

	if request.method=="POST":
		login_form =LoginForm(request.POST)

		if  login_form.is_valid():
			username=login_form.cleaned_data['username']
			password=login_form.cleaned_data['password']

			user=auth.authenticate(username=username,password=password)

			if user is not None:
				auth.login(request,user)
				return redirect('loan:payment')

			else:
				messages.info(request,"Given Credentials not matching!!")
				return redirect('accounts:login')


	else:
		login_form =LoginForm(request.POST)


	context={
				'login_form':login_form,
	}
	return render(request,template_name,context)


def logout(request):
	auth.logout(request)
	return redirect('/')