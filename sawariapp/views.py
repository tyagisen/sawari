from django.shortcuts import render
from .forms import DriverForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def sign(request):
    if request.method == 'POST':
        fm = DriverForm(request.POST)
        message1 = request.POST['name']
        message3 = request.POST['phone']
        message4 = request.POST['vehicle_type']
        message = "Name: " + message1 + "\n" + "Phone: " + message3 + "\n" + "Vehicle Type: " + message4
        if fm.is_valid():
            fm.save()
            send_mail(
                'Driver Form',
                message,
                settings.EMAIL_HOST_USER,
                ['tyagisen@gmail.com'],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, 'You Are Registerd')
            fm = DriverForm()
    else:
        fm = DriverForm()
    return render(request, 'index.html', {'form': fm})
