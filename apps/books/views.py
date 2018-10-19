from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.log_reg.models import User
from .models import Author, Book, Review

def index(request):
    data = {
        'user': User.objects.get(email=request.session['email']),
        'reviews': Review.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, "books/home.html", data)

def add_book(request):
    data = {
        'authors': Author.objects.all()
    }
    return render(request, "books/add.html", data)

def book(request):
    return render(request, "books/book.html")

def new_book(request):
    if request.method == 'POST':
        if len(request.POST['author_new']) > 0:
            author = request.POST['author_new']
            Author.objects.create(name=author)
        else:
            author = request.POST['author_names']
        Book.objects.create(title=request.POST['title'], author=Author.objects.get(name=author), user=User.objects.get(email=request.session['email']))
        Review.objects.create(review=request.POST['review'], rating=request.POST['stars'], user=User.objects.get(email=request.session['email']), book=Book.objects.last())
        return redirect('/books')
    return redirect('/books/new')
def add_review(request):
    return redirect('/books/1')