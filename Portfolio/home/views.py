from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    #return HttpResponse("This is homepage(/)")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("This is about")
    return render(request, 'about.html')

def projects(request):
    #return HttpResponse("This is projects")
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print('the data has been written to DB')
    #return HttpResponse("This is contact")
    return render(request, 'contact.html')