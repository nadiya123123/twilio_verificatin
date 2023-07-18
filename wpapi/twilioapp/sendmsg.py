from twilio.rest import Client
from django.conf import settings

client=Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)


message=client.messages.create(to='whatsapp:+91xxxxxxx',
                               from_='whatsapp:+14155238886',
                               body="test ")




#https://timberwolf-mastiff-9776.twil.io/demo-reply