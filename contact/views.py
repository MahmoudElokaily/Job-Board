from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def send_message(request):
    my_info = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )

    context = {
        'myInfo' : my_info,
    }
    return render(request , 'contacts/contact.html' , context)