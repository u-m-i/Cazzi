#Utilities
from datetime import datetime

# Django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = 
    {
        'name' : 'Yami',
        'user' : 'Tanaka Yukio'
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
        {
        'name' : 'Our',
        'user' : 'Tanaka Yukio',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
        {
        'name' : 'Never',
        'user' : 'Tanaka Yukio',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },

def list_posts(request):
    """list the existing posts
    """
    content = []
    for post in posts:
        content.append(f"""
        """)
    return HttpResponse(str(posts))
    
