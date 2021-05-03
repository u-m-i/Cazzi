""" Views of cazzi
"""
#utilities
from datetime import datetime

#Django
from django.http import HttpResponse
from django.http import JsonResponse
import json


def hello_there(request):
    """Return the time zip a gretting
    """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Konbanwa! your time is currently {now}')


def otsu(request):
    """Otsuuu
    """
    # numbers = sorted([int(number) for number in request.GET['numbers'].split(',')]) 
    # return JsonResponse({"numbers" : numbers}, json_dumps_params={'indent': 4 }, safe=False)
    numbers = sorted([int(number) for number in request.GET['numbers'].split(',')]) 
    data = {
        'status' : 'ok',
        'numbers' : numbers,
        'message' : 'Sugoi des, successfully sorted'
    }
    return HttpResponse(
        json.dumps(data),
        content_type='application/json')

def otsu_mayor(request,namae,age):
    """If you are a underage, will raise a warning, otherwise, you'r welcom
    """
    if age > 15:
        return HttpResponse(f'otsuuuu {namae} welcom to Cazzi')
    else:
        return HttpResponse(f'yo bro, gtf of here')

