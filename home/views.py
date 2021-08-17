from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Services
from django.contrib import messages

# Create your views here.
def index(request):
    services = Services.objects.all()
    return render (request,"index.html",{'params':services})
    #return HttpResponse("This is a home page")

def about(request):
    return render (request,"about.html")

def services(request):
    services = Services.objects.all()
    #params = {'services' : services}
    return render (request,"services.html",{'params' : services})
    
def contact(request):
    if request.method == "POST":
        name       = request.POST.get('name')
        email_id   = request.POST.get('email_id')
        mobile_no  = request.POST.get('mobile_no')
        message    = request.POST.get('message')
        contact    = Contact(name=name, email_id=email_id, mobile_no=mobile_no, message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your messages has been succesfully sent.')
        
    return render (request,"contact.html")
