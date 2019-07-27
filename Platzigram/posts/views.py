"""Posts views."""
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title' : 'Mont Blank',
        'user' : {
            'name' : 'Yesica Cortez',
            'picture' : 'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'title' : 'Mont Blank',
        'user' : {
            'name' : 'Yesica Cortez',
            'picture' : 'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'title' : 'Mont Blank',
        'user' : {
            'name' : 'Yesica Cortez',
            'picture' : 'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/200/200/?image=1036',
    },
]

def list_posts(request):
    """List existing posts."""
    return render(request,'feed.html', { 'posts' : posts })