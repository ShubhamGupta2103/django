from django.shortcuts import render
from matplotlib.pyplot import *

# Create your views here.

def index(request):
    ctx = {}

    ctx['title'] = 'Home'
    return render(request, 'blog/index.html')
