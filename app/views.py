from django.shortcuts import render
from .models import Artista, Album, Musica

def index(request):
	album = Album.objects.filter(pk=3)
	artista = Artista.objects.filter(album=album)
	musica = Musica.objects.filter(album=album)
	return render(request, 'index.html', {'artista': artista, 'album': album, 'musica': musica})