from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Album, Booking, Contact
from django.template import loader

# Create your views here.
def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_album = ["<li>{}</li>".format(album) for album in albums]
    message = "<ul>{}</ul>".format("\n".join(formatted_album))
    template = loader.get_template('store/index.html')
    return HttpResponse(template.render(request=request))

def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_album = ["<li>{}</li>".format(album) for album in albums]
    message = "<ul>{}</ul>".format("\n".join(formatted_album))
    return HttpResponse(message)

def details(request, album_id):
    id = int(album_id)
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = f"Cette album se nomme {album.title} et a ete ecrit par {artists}"
    return HttpResponse(message)
def search(request):
    query = request.GET.get('query')
    if not query:
        message= "Vous n'avez rien entre"
    else:
        albums = Album.objects.filter(title__icontains=query)
        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)
        if not albums.exists():
            message = "Nous n'avons trouve aucun album correspondant"
        else:
            albums = ["<li>"+album.title+"</li>" for album in albums]
            message = """Les albums correspondantes sont :
            <ul>
                {}
            </ul>""".format("\n".join(albums))
    return HttpResponse(message)