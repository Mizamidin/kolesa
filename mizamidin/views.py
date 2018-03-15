from django.shortcuts import render
import datetime

from .models import Car, Seller, MarkInstance, Type

def index(request):

    num_cars=Car.objects.all().count()
    num_instances=MarkInstance.objects.all().count()
    num_instances_available=MarkInstance.objects.filter(status__exact='a').count()
    num_sellers=Seller.objects.count()  
    time=datetime.datetime.now()
    n_hour=time.hour
    n_minute=time.minute
    n_second=time.second
    n_year=time.year
    n_month=time.month
    n_day=time.day
    w_day=time.weekday
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    return render(
        request,
        'index.html',
        context={'num_cars':num_cars,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_sellers':num_sellers,'num_visits':num_visits,'hour':n_hour,'minute':n_minute,'second':n_second,'year':n_year,'month':n_month,'day':n_day,'weekday':w_day},
    )
from django.views import generic

class CarListView(generic.ListView):
    model = Car
    paginate_by = 2
class CarDetailView(generic.DetailView):
    model = Car
class SellerListView(generic.ListView):
    model = Seller
    paginate_by = 2
class SellerDetailView(generic.DetailView):
    model = Seller

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Seller

class SellerCreate(CreateView):
    model = Seller
    fields = '__all__'
    initial={'date_of_birth':'01/06/1997',}

class SellerUpdate(UpdateView):
    model = Seller
    fields = ['first_name','last_name','date_of_birth','phone']

class SellerDelete(DeleteView):
    model = Seller
    success_url = reverse_lazy('sellers')