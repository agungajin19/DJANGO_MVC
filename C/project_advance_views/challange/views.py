from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentor, Mentee, Blog

# Create your views here.
def index(request):
    return render(request, 'challange/index.html', {})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'challange/blog.html', {'blogs':blogs})

def mentee(request):
    mentees = Mentee.objects.all()
    return render(request, 'challange/mentee.html', {'mentees':mentees})

def mentor(request):
    mentors = Mentor.objects.all()
    return render(request, 'challange/mentor.html', {'mentors':mentors})

def author(request):
    return render(request, 'challange/author.html', {})
