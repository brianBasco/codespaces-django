from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def clicked(request):
    if request.method == "POST":
        response = HttpResponse("OK !!!!!!", 200)
        response["HX-Trigger"] = "showMessage"
        return response
    
