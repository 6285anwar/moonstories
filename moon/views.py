from django.shortcuts import render,redirect
from .models import *
from datetime import date 
from datetime import datetime

# Create your views here.

def index(request):
    books = Story.objects.all()
    return render(request, 'index.html',{"Books":books})
def books(request):
    books = Story.objects.all()
    return render(request, 'books.html',{"Books":books})
def read(request,id):
    story=Story.objects.get(id=id)
    return render(request, 'read.html',{"story":story})


def dashboard(request):
    storys = Story.objects.all()
    return render(request, 'bookadd.html',{"storys":storys})

def addbook(request):
    if request.method =='POST':
        bookname = request.POST["bookname"]
        link = request.POST["link"]
        content = request.POST["shortcontent"]
        image = request.FILES['image']

        todaydate = datetime.now()
        
        status = "Show"

        src=link[13:-11]
        s = Story()
        
        s.storyname = bookname
        s.storysrc = src
        s.content = content
        s.bookphoto = image
        s.date = todaydate
        s.status = status

        s.save()
        return redirect(dashboard)


def bookdelete(request,id):
    s = Story.objects.get(id=id)
    s.delete()
    return redirect(dashboard)

def bookhide(request,id):
    s = Story.objects.get(id=id)
    s.status = "Hidden"
    s.save()
    return redirect(dashboard)
def bookshow(request,id):
    s = Story.objects.get(id=id)
    s.status = "Show"
    s.save()
    return redirect(dashboard)
    
def latest_yes(request,id):
    s = Story.objects.get(id=id)
    s.latest = "yes"
    s.save()
    return redirect(dashboard)

def latest_no(request,id):
    s = Story.objects.get(id=id)
    s.latest = "no"
    s.save()
    return redirect(dashboard)