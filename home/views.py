from django.shortcuts import render

def index(request):
    """ a view to return the index page """
    return render(request, 'home/index.html')

