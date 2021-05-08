#Utilities
from datetime import datetime

# Django
from django.shortcuts import render

# Create your views here.

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Diego Norrea',
            'picture': 'https://i1.sndcdn.com/avatars-RePbt181zZmasG8Q-wrGlhg-t500x500.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ytimg.com/vi/67MsNUdKJG4/hqdefault.jpg',
    }
]
def list_posts(request):
    """list the existing posts
    """
    return render(request,'feed.html', {'posts': posts}) #render recibe el objeto request, luego da el template a la vista
                                                         # luego de recibir el template, recibe el contexto que el pasemos.
    
