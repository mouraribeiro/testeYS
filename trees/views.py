from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.

class AccountCreate(ListView):
    model = Account
def home(self, request):
    user = self.request.user
    return HttpResponse("olá")



# @login_required
# def final(request):
#     bookings = Sign.objects.filter(user=request.user)
#     return render(request, 'datas/final.html', {'bookings': bookings})