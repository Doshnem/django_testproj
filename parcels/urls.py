from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='parcels'),
    #path('<int:parcel_id>', views.parcel, name='parcel'),
    path('search', views.search, name='search')

]