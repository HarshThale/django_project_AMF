from django.shortcuts import render
from django.http import HttpResponse
from food.models import Item

# Create your views here.

def index(request):
    itemlist = Item.objects.all()
    
    context = {              #dictionary
        'itemlist':itemlist   #'itemlist': -->key
    }
    
    return render(request, 'food/index.html', context)  #render the request food/index
    
def detail(request, item_id):  
    item = Item.objects.get(pk=item_id)

    context = {
        'item':item
    }
    
    return render(request, 'food/detail.html', context)