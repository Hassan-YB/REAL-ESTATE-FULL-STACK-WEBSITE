from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.db import connection

company=PropertyCompany.objects.all()
#@login_required
def index(request):
    properties=Advertisement.objects.filter(ad_price_type="Featured listing $20")
    pro=Advertisement.objects.filter(ad_price_type="Regular listing $5")[:3]
    if request.method=="POST":
        form=Submitpropertyform(request.POST)
        Newsform=Newsletterform(request.POST)
        if form.is_valid():
            ad=Advertisement()
            ad.type=form.cleaned_data['type']
            ad.listing_type=form.cleaned_data['listing_type']
            ad.title=form.cleaned_data['title']
            ad.price=form.cleaned_data['price']
            ad.id=form.cleaned_data['id']
            ad.bedrooms=form.cleaned_data['bedrooms']
            ad.bathrooms=form.cleaned_data['bathrooms']
            ad.floor_number=form.cleaned_data['floor_number']
            ad.area=form.cleaned_data['area']
            ad.built_up_year=form.cleaned_data['built_up_year']
            ad.price=form.cleaned_data['price']
            ad.neigborhood=form.cleaned_data['neigborhood']
            ad.ad_price_type=form.cleaned_data['ad_price_type']
            ad.country=form.cleaned_data['country']
            ad.state=form.cleaned_data['state']
            ad.city=form.cleaned_data['city']
            ad.expiry=form.cleaned_data['expiry']
            ad.description=form.cleaned_data['description']
            ad.street_and_house_no=form.cleaned_data['street_and_house_no']
            ad.owner=form.cleaned_data['owner']   
            ad.save()
            return redirect('/')
        if Newsform.is_valid():
            object=Newsletter()
            object.email=Newsform.cleaned_data['email']
            object.save()
            return redirect('/')
        
    return render(request,'sailor/home.html',{'properties':properties,'company':company,'pro':pro})

def contact(request):
    return render(request,'sailor/contact.html',{'company':company})

def agent_profile(request):
    return render(request,'sailor/agent_profile.html',{'company':company})

def details(request):
    return render(request,'sailor/details.html',{'company':company})

def index_map(request):
    return render(request,'sailor/index-map.html',{'company':company})

def pricing(request):
    return render(request,'sailor/pricing.html',{'company':company})

def registration(request):
    return render(request,'sailor/registration.html',{'company':company})

def results_grid(request):
    return render(request,'sailor/results_grid.html',{'company':company})

def results(request):
    if request.method=="POST":
        country=request.POST['country']
        city=request.POST['city']
        listing=request.POST['listing_type']
        bedrooms=request.POST['bedrooms']
        se=Advertisement.objects.filter(country=country,city=city,listing_type=listing,bedrooms=bedrooms)
        return render(request,'sailor/results.html',{'company':company,'search':se})
    return render(request,'sailor/results.html',{'company':company})

def search_users(request):
    return render(request,'sailor/search_users.html',{'company':company})

def submit(request):
    return render(request,'sailor/sumbit.html',{'company':company})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def detail(request,id):
    property_detail=get_object_or_404(Advertisement,pk=id)
    return render(request,'sailor/details.html',{'property_detail':property_detail,'company':company})






