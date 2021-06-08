from website import urls
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html',{})
def contact(request):
    if request.method=='POST':
        sender_name=request.POST['message-name']
        email_address=request.POST['message-email']
        message=request.POST['message']
        send_mail(
            sender_name, #subject
            message, #message
            email_address,#From email
            ['farhanisrak1503001@gmail.com'],#To email
            fail_silently=False
        )
        messages.success(request,'Email Sent Successfully')
        return render(request,'contact.html',{})

    else:
        return render(request,'contact.html',{})
