from django.shortcuts import render,redirect
from . import models as m
from django.contrib import messages
# Create your views here.
def index(request):
    contex = {
        'categories' : m.Categories.objects.order_by('created_at')
    }
    return render(request, 'categories/index.html', contex)

def create(request):
    return render(request, 'categories/create.html')

def store(request):
    errors = []
    if request.method == 'POST':
        try:
            name        = request.POST['name']
            if len(name) == 0:
               errors.append("Fields cannot be blank.")
               messages.error(request, "Fields cannot be blank")
                    
            if len(errors) == 0 :
                categories          = m.Categories()
                categories.name     = name
                categories.save()
                return redirect('categories:index')
        except:
            messages.error(request, 'Invalid Input')
    return redirect('categories:create')

def edit(request, cat_id):
    contex = {
        'categori' : m.Categories.objects.get(id=cat_id)
    }
    return render(request, 'ecategories/edit.html', contex)

def update(request, cat_id):
    errors = []
    if request.method == "POST":
        name                = request.POST['name']
        try:
            if len(name) == 0:
               errors.append("Fields cannot be blank.")
               messages.error(request, "Fields cannot be blank.")
            
            if len(errors) == 0:
                categori        = m.Categories.objects.get(id=cat_id)
                categori.name   = name 
                categori.save()
                return redirect('categories:index')
        except:
            raise

def delete(request, cat_id):
    categori        = m.Categories.objects.get(id=cat_id)
    categori.delete()
    return redirect('categories:index')
