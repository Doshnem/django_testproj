from django.shortcuts import render
from .models import Parcel

def index(request):
    parcels = Parcel.objects.all()

    context = {
        'parcels': parcels
    }
    return render(request, 'parcels/parcels.html', context)

def parcel(request, parcel_id):
    return render(request, 'parcels/parcel.html')

def search(request):
    return render(request, 'parcels/search.html')