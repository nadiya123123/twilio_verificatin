from django.shortcuts import render,HttpResponse
from twilio.rest import Client
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

client=Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)

@csrf_exempt


def bot(request):
       message= request.POST["Body"]
       sender_name=request.POST["ProfileName"]
       sender_number=request.POST["From"]
       if message=='Hi':
            client.messages.create(to='whatsapp:+91xxxxxxx',
                                         from_='whatsapp:+14155238886',
                                         body=f"Hello,{sender_name}")

       return HttpResponse("hello")
