from django.shortcuts import render
from about.models import About
# Create your views here.

def home(request):
	info = About.objects.all()
	return render(request,'home.html',{'info':info})