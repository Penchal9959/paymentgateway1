from django.shortcuts import render
from django.http import HttpResponse
from .forms import PaymentForm
from .models import Payment

# Create your views here.


def payment_make_view(request):

    # if request.method == "POST"
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PaymentForm()
    context = {
        'form': form
    }
    return render(request, "payments/payment_make.html", context)


def thankyou(request):
	return render(request, 'payments/thankyou.html')