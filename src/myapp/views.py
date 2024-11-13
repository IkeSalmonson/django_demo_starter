from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
## The app has to be declared on project settings.py  INSTALLED_APPS 
def home(request):
    return render(request, 'home.html')
    #return HttpResponse('hello World ') ## version without template
    ## function is called by app urls.py 

def todos(request):
    items = TodoItem.objects.all() ## get all from db 
    return render(request, 'todos.html', {"todos":items})
    ## function is called by app urls.py     