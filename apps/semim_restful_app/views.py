from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show

def create(request):
    return render(request,'create.html')

def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'],description=request.POST['description'],release_date=request.POST['release_date'],network=request.POST['network'])
        show = Show.objects.last()
        return redirect('/shows/'+str(show.id))

def edit_show(request,id):
    show = Show.objects.get(id=id)
    show.title=request.POST['title']
    show.description=request.POST['description']
    show.release_date=request.POST['release_date']
    show.network=request.POST['network']
    show.save()
    return redirect('/shows/'+str(show.id))

def delete(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

    
def allShows(request):
    all_shows = Show.objects.all()
    context = {
        "all_shows" : all_shows
        
    }
    
    return render(request,'allShows.html', context)

def edit(request,id):
    context = {
        "show" : Show.objects.get(id=id)

        }
    
    return render(request, 'edit.html', context)

def read(request,id):
    show = Show.objects.get(id=id)
    context = {
        "show" : show
        
    }
    return render(request, 'read.html', context)

