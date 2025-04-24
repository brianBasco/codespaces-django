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

def contacts(request):
    ordre = request.GET.get('ordre', 'asc')
    """
    if ordre == 'desc':
        contacts = Contact.objects.order_by('-nom')
    else:
        contacts = Contact.objects.order_by('nom')
    """
    if request.htmx:
        return render(request, 'liste_contacts.html', {'contacts': contacts})
    return render(request, 'contacts.html', {'contacts': contacts})
    
def search(request):
    return render(request, "search.html")