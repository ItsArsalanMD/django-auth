from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(req):
    return render(req, 'login.html')

@login_required
def home(req):
    return render(req, 'home.html')