
from django.shortcuts import render
from .verify import MessaHandler
import random



def generate_otp():
    # Generate a 6-digit OTP
    return str(random.randint(100000, 999999))


def send_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = generate_otp()

        messa_handler = MessaHandler(phone_number, otp)
        messa_handler.send_otp_on_phone()

        return render(request, 'otp_sent.html', {'phone_number': phone_number})

    return render(request, 'send_otp.html')