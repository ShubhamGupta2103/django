from django.shortcuts import render, HttpResponse
from .models import Tag, Image

# Create your views here.
def index(request):
    categories = Tag.objects.all() # get all the categories
    images = Image.objects.all()        # get all the images
    ctx = {
        'categories': categories,
        'images': images,
        'title' : 'Games',
    }

