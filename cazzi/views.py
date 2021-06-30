# Django
from django.http import HttpResponse

# Utilities
from datetime import  datetime

def feed(request):
    """ Return the feed
    """

    return 

def static_page(request):
    """
    Return a greeting

    """

    return  HttpResponse("Loco, i cameback to learn and make my copy of instagram")

def your_time(request):
    """ Return the current server time
    """
    now = datetime.now().strftime('%b, %dth, %Y - %H:%M hrs ')

    return HttpResponse(f"Hello there, your current time is {now}")

def converter(request):
    """Sort an array of numbers"""

    numbers = request.GET["numbers"]
    breakpoint()
    return HttpResponse(str(numbers))