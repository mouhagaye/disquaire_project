from django.shortcuts import render
from django.http import HttpResponse
from .models import ALBUMS

# Create your views here.
def index(request):
    return HttpResponse("Salut tout le monde")
def listing(request):
    albums = ['<li>{}</li>'.format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)
def details(request, album_id):
    id = int(album_id)
    album = ALBUMS[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = f"Cette album se nomme {album['name']} et a ete ecrit par {artists}"
    return HttpResponse(message)
def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demande"
    else:
        albums = [
            album for album in ALBUMS
            if  query in " ".join(artist['name'] for artist in album['artists'])
        ]
        if len(albums) == 0:
            message = "Nous n'avons trouve aucun album"
        else:
            albums = ["<li>"+album['name']+"</li>" for album in albums]
            message = """Les albums correspondantes sont :
            <ul>
                {}
            </ul>""".format("\n".join(albums))
    return HttpResponse(message)