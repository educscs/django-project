import json
from django.http import HttpResponse
from .models import Album, Artist, Song
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as lg


# Create your views here.

@login_required
def album_id(request, id):
    album = Album.objects.get(id=id)
    context = {'album': str(album)}
    return HttpResponse(str(context))

@login_required
def artist_id(request, id):
    artist = Artist.objects.get(id=id)
    print(artist)
    context = {'artist': str(artist)}
    return HttpResponse(str(context))

@login_required
def search_songs_by_author(request):
   query = request.GET['q']
   album_results = Album.objects.filter(artist__name__icontains = str(query))
   all_songs = dict()
   for album in album_results.all():
     song_results = Song.objects.filter(album__title__icontains = str(album))
     list_song=list()
     for song in song_results.all():
        print(song.title)
        list_song.append(song.title)
     all_songs[album.title] = list_song
   return HttpResponse(str(all_songs))

@csrf_exempt
def login(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       email = data.get("email")
       password = data.get("password")
       user = authenticate(email=email, password=password)
       token, _ = Token.objects.get_or_create(user=user)
       return HttpResponse({'token': token.key})

def logout(request):
    if request.method == 'POST':
       lg(request)
    return HttpResponse("Successful logout")