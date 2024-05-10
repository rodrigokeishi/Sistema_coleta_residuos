from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def homeresiduos(request):
    return render(request, "homeresiduos.html")
