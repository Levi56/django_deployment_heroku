from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def VIEW(request):
	return render(request, "APP/EZ.html", {})


def index(request):
	template = "index.html"
	context = {}
	return render(request, template, context)



