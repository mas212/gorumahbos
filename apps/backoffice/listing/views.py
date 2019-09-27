from django.shortcuts import render, redirect
from . import models as m
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.method == 'GET': 
        listings   = m.Listing.objects.all()
        return render(request, 'listing/index.html', {'listings': listings})

def create(request):
    return render(request, 'listing/create.html')

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
            
            listing                 = m.Listing()
            listing.name            = name
            listing.price           = price
            listing.description     = description
            listing.qtyRoom         = qtyRoom
            listing.photo           = filename
            listing.save()
            return redirect('listing:index')
                
        except:
            raise
def edit(request, listing_id):
    listing         =  m.Listing.objects.get(id=listing)
    return render(request, 'listing/edit.html', {'listing' : listing})
def delete(request, listing_id):
    listing = m.Listing.objects.get(id=listing_id)
    listing.delete()
    return redirect('listing:index')
