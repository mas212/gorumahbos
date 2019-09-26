from django.shortcuts import render ,redirect
from . import models as m
from django.contrib import messages
# Create your views here.
def index(request):
    contex = {
        'locations' : m.Location.objects.order_by('created_at')
    }
    return render(request, 'location/index.html', contex)

def create(request):
    return render(request, 'location/create.html')

def store(request):
    errors  = []
    if request.method == 'POST':
        try:
            name        = request.POST['name']
            if len(name) == 0:
                errors.append("Fields cannot be blank.")
                messages.error(request, "Fields cannot be blank")
            if len(errors) == 0 :
                location        = m.Location()
                location.name   = name
                location.save()
                return redirect('location:index')
        except:
            messages.error(request, 'Invalid Input')
    return redirect('location:create')

def edit(request, location_id):
    contex = {
        'location' : m.Location.objects.get(id=location_id)
    } 
    return render(request, 'location/edit.html', contex)

def update(request, location_id):
    errors = []
    if request.method == 'POST':
        name    = request.POST['name']
        try:
            if len(name) == 0 :
                errors.append("Fields cannot be blank.")
                messages.error(request, "Field cannot be blank")
            if len(errors) == 0 :
                location    = m.Location.objects.get(id=location_id)
                location.name   = name
                location.save()
                return redirect("location:index")
        except:
            messages.error(request, 'Invalid Input')
            return render(request, 'location/edit.html', contex)
    return redirect("location:index")
    
def delete(request, location_id):
    location    = m.Location.objects.get(id=location_id)
    location.delete()
    return redirect('location:index')
