from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics

from contact.models import Contact
from contact.serializers import ContactSerializer


# Create your views here.


class ContactApiView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def index(request):
        if request.method == "POST":
            message = request.POST['message']
            email = request.POST['email']
            name = request.POST['name']
            send_mail(
                name,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False)
            return HttpResponse("<h2><b>Thank for contact us<b></h2>")
        return render(request, 'index.html')
