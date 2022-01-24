from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    DEFAULT_PW_LEN = 12

    # default password generator character bank
    chars = list('abcdefghijklmnopqrstuvwxyz')

    # add characters to the bank if requested
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special characters'):
        chars.extend(list('~!@#$%^&*()_+'))

    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
    
    # get the requested pw length
    pw_len = int(request.GET.get('length', DEFAULT_PW_LEN))
    pw = ""

    # create the password
    for i in range(pw_len):
        pw += random.choice(chars)
    
    return render(request, 'generator/password.html', {'password':pw})

def about(request):
    return render(request, 'generator/about.html')