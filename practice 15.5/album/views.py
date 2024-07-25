from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
# Create your views here.
def add_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'album/add_album.html',{'form' : form})

def delete_album(request, id):
    album = Album.objects.get(id=id)
    album.delete()
    return redirect('home')

def edit_album(request, id):
    album = Album.objects.get(id=id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'album/edit_album.html', {'form': form})
