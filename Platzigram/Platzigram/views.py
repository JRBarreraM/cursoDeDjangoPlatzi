"""Platzigram URLs module"""
#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime

import json

def helloWorld(request):
    """Return a greeting"""
    return HttpResponse('Oh, current server time is: {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sayHi(request,name,age):
    """Return a greeting"""
    if age < 12:
        message = 'sorry {} are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)

def sortIntegers(request):
    """"Returns a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sortedNumbers = sorted(numbers)
#    import pdb; pdb.set_trace()
    data = {
        'status' : 'ok',
        'numbers' : sortedNumbers,
        'message' : 'Integers sorted succesfully.'
    }
    return HttpResponse(
        json.dumps(data,indent=3),
        content_type='application/json'
    )