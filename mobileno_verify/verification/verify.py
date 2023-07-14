from twilio.rest import Client
from django.conf import settings


class MessaHandler:

    phone_number=None
    otp=None

    def __init__(self,phone_number,otp) -> None:
        self.phone_number=phone_number
        self.otp=otp
    def send_otp_on_phone(self):
        client = Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(body=f'Hi your otp is:{self.otp}',
                                         from_='+12517148068',
                                         to=self.phone_number
                                         )

