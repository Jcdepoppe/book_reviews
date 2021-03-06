from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "log_reg/index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        pass_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print(pass_hash)
        User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=pass_hash)
        user = User.objects.last()
        # Better to use user id in this case because a user could change their email
        request.session['email'] = user.email
        request.session['alias'] = user.alias
        request.session['success'] = "Thank you for registering!"
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method =="POST":
        errors = User.objects.validLogin(request.POST, request)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = User.objects.get(email=request.POST['emaillogin'])
        request.session['email'] = request.POST['emaillogin']
        request.session['alias'] = user.alias
        return redirect('/success')
    return redirect('/')

def user(request):
    return render(request, 'log_reg/user.html')

def success(request):
    return redirect('/books')