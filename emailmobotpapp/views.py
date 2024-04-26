from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
import requests


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'input.html')
class Send(View):
    def get(self,request):
        subject='thank for contacting'
        otp=str(random.randint(100000,999999))
        print(otp)
        from_email=settings.EMAIL_HOST_USER
        email=request.GET["t1"]
        mobno="+91"+request.GET["t2"]
        to_list=[email]
        send_mail(subject,otp,from_email,to_list,fail_silently=False)
        resp = requests.post('https://textbelt.com/text', {
            'phone': 'mobno',
            'message': 'otp',
            'key': '87b6c2c1b021f252dd38f95f3b631ecd2cda4d17fnQABurTqMTHSaTKrUg3w6hqa',
        })
        print(resp.json())

        return HttpResponse("Email sent successfully")