from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe
# Create your views here.
stripe.api_key = 'sk_test_51IC2qyA1yapRcmMMe2xQJq1Tky7mdaZQiyLUo45pIvka9lZQkMD9TSq2Ej3eaI61E1x7Rl6cnLEaZXSMzjNNcPrr00XxgvaHuT'

def index(request):
	return render(request, 'index.html')


def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

		amount=request.POST['amount']

		customer=stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
		)
		charge=stripe.Charge.create(
			customer=customer,
			amount=500,
			currency="usd",
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'success.html', {'amount':amount})