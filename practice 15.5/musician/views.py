from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician

from album.models import Album

def homepage(request):
    albums = Album.objects.all()
    return render(request, 'musician/home.html',{'albums':albums})

def add_musician(request):
    form = MusicianForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'musician/add_musician.html',{'form' : form})

def edit_musician(request,id):
    musician = Musician.objects.get(id=id)
    form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'musician/edit_musician.html',{'form' : form})