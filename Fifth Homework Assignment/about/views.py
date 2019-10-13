from django.shortcuts import render
from .models import About


# Create your views here.


def about_us(request):
	info = About.objects.all()

	template='about/aboutus.html'

	context={
				'info':info,
	}

	return render(request, template, context)