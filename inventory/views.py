from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import House


def home(request):
    context = {
        'title': 'Hogwarts Inventory',
        'subtitle': 'Track your magical belongings with ease.',
        'items': [
            'Wand',
            'Invisibility Cloak',
            'School Supplies',
            'Quidditch Gear',
        ],
    }
    return render(request, 'inventory/home.html', context)


class HouseListView(ListView):
    model = House
    template_name = 'inventory/house_list.html'
    context_object_name = 'houses'
    ordering = ['name']


class HouseDetailView(DetailView):
    model = House
    template_name = 'inventory/house_detail.html'
    context_object_name = 'house'
