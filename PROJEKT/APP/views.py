from django.shortcuts import render

def VIEW(request):
	return render(request, "APP/EZ.html", {})

# Create your views here.
