from django.http.response import HttpResponse
from django.shortcuts import render

from travello.models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Rajkot'
    dest1.desc = 'Rangilu rajkot'
    dest1.price = '1000'
    dest1.img = 'destination_1.jpg'
    dest1.offer=True
    dest2 = Destination()
    dest2.name = 'Ahmedabad'
    dest2.desc = 'City which always in the sleep'
    dest2.price = '500'
    dest2.img = 'destination_2.jpg'
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Hyderabad'
    dest3.desc = 'Famous for Biryani'
    dest3.price = '700'
    dest3.img = 'destination_3.jpg'
    dest3.offer=False
    
    dests = [dest1,dest2,dest3]
    return render(request,'index.html', {'dests':dests})

