"""Platzigram URLs module"""
#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime

def helloWorld(request):
    """Return a greeting"""
    return HttpResponse('Oh, current server time is: {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi(request):
    """"Hi."""
    numbers = request.GET['numbers']
    import pdb; pdb.set_trace()
    return HttpResponse(str(numbers))