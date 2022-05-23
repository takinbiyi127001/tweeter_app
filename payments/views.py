from django.shortcuts import render
from django.views.generic.base import TemplateView
import stripe
import environ

env = environ.Env()

# reading .env file
environ.Env.read_env()

stripe.api_key = env.str('STRIPE_SECRET_KEY')  # use your secret key


# Create your views here.

class PaymentPageView(TemplateView):
    template_name = 'payment.html'


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,  # amount is in cents.
            currency='aud',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
