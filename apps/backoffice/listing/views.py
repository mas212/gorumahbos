from django.shortcuts import render, redirect
from . import models as m
from apps.backoffice.categories.models import Categories
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    if request.method == 'GET': 
        listings        = m.Listing.objects.all()
        contex ={
            'listings' : listings
        }
        return render(request, 'listing/index.html', contex)

def create(request):
    contex = {
        'categories' : m.Categories.objects.all()
    }
    return render(request, 'listing/create.html', contex)

def store(request):
    errors = []
    if request.method == 'POST' and request.FILES['photo']:
        myfile              = request.FILES['photo']
        fs                  = FileSystemStorage()
        filename            = fs.save(myfile.name, myfile)
        uploaded_file_url   = fs.url(filename)
        try:
            name                = request.POST['name']
            price               = request.POST['price']
            description         = request.POST['description']
            qtyRoom             = request.POST['qtyRoom']
            category            = request.POST['category']

            listing                 = m.Listing()
            listing.name            = name
            listing.price           = price
            listing.category_id     = int(category)
            listing.description     = description
            listing.qtyRoom         = qtyRoom
            listing.photo           = filename
            listing.save()
            return redirect('listing:index')      
        except:
            raise
def edit(request, listing_id):
    context = {
        'listing' : m.Listing.objects.get(id=listing_id)
    }
    return render(request, 'listing/edit.html', context)
def update(request, listing_id):
    errors = []
    if request.method == 'POST' and request.FILES['photo']:
        myfile              = request.FILES['photo']
        fs                  = FileSystemStorage()
        filename            = fs.save(myfile.name, myfile)              
        try:
            name                = request.POST['name']
            price               = request.POST['price']
            description         = request.POST['description']
            qtyRoom             = request.POST['qtyRoom']

            listing             = m.Listing.objects.get(id=listing_id)
            listing.name        = name
            listing.price       = price
            listing.description = description
            listing.qtyRoom     = qtyRoom
            listing.photo       = filename
            listing.save()
            return redirect('listing:index')
        except:
            raise

def delete(request, listing_id):
    listing = m.Listing.objects.get(id=listing_id)
    listing.delete()
    return redirect('listing:index')
