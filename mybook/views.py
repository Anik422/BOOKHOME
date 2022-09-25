from multiprocessing import context
from django.shortcuts import render, redirect
from mybook.models import Author, Book, District, Branches
from mybook.forms import Shippingform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate
from django.db.models import Q
from django.http import HttpResponseRedirect
# user book pass 12345
# Create your views here.


def home(request):
    brjs = District.objects.all()
    return render(request, 'home.html', {'bjs':brjs})


def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user, password=password)
        
        if user is not None:
            
            auth_login(request,user)
            return redirect('view_authors')
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                return redirect('/')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'registration/register.html', {'messages': messages})





def view_authors(request):
    author_names = Author.objects.all()
    return render(request, 'auther.html', {"author_names": author_names})

def author_books(request, id):
    author_name = Author.objects.get(id=id)
    author_books = Book.objects.filter(book_author=author_name)
    return render(request, 'author_books.html', {
        
        "author_books": author_books
        })

def branch(request):
    brjs = District.objects.all()
    return render(request, 'branche.html', {'bjs': brjs})
def branches(request,area):
    area=District.objects.get(id=area)
    braju=Branches.objects.filter(DistricNM=area)
    return render(request, 'branche.html',{'brej':braju})


def purchase(request):
    if request.method == 'POST':
        pform = Shippingform(request.POST)
        if pform.is_valid():
            pform.save()
            return redirect('despatch',)  # despach
        else:
            messages.info(request, 'Fill form Mantory')
        context['form'] = pform

    return render(request, 'purchase.html', context)
def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Book.objects.all().filter(Q(book_name__contains=query)| Q(desc__contains=query))

    return render(request, 'search.html', {'qr': query, 'pr': prod})
def despatch(request):
    return render(request,'despatch.html')

