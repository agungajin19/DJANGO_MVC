from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'challange/index.html', {})


def blog(request):
    return render(request, 'challange/blog.html', {})

def mentee(request):
    return render(request, 'challange/mentee.html', {})

def mentor(request):
    return render(request, 'challange/mentor.html', {})

def author(request):
    return render(request, 'challange/author.html', {})
