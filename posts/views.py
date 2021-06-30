"""Posts views"""


from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

posts = [
    {
        "title": "Navigate",
        "user": {
            "name": "Yami",
            "picture": "https://vocadb.net/Artist/Picture/59773",  
        },
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "photo" :  "https://q-xx.bstatic.com/xdata/images/hotel/840x460/78809294.jpg?k=cf850d507a9671cf7ff85d598435ea329a28cd4f1b1abc25c1892c91156d36ad&o=",
    },
    {
        "title": "Aniversary",
        "user": {
            "name": "Miguel",
            "picture": "https://i.pinimg.com/474x/55/f2/63/55f26318b0dc191f97557ead146acdf3.jpg" ,      
        },
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "photo" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLQOSqoj_D8MhtjUB8t551oWaeKpQvSWgRhQ&usqp=CAU",
    },
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
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
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

def list_post(request):
    """List the lastest posts"""
    return render(request, "/home/umi/Documents/Projects/Platzi/Cazzi/templates/posts/feed.html", {"posts": posts})
