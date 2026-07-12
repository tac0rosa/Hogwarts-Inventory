from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import HouseForm, ProfessorForm
from .models import House, Professor


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


class HouseCreateView(CreateView):
    model = House
    form_class = HouseForm
    template_name = 'inventory/house_form.html'
    success_url = reverse_lazy('house_list')


class HouseUpdateView(UpdateView):
    model = House
    form_class = HouseForm
    template_name = 'inventory/house_form.html'

    def get_success_url(self):
        return reverse_lazy('house_detail', kwargs={'pk': self.object.pk})


class HouseDeleteView(DeleteView):
    model = House
    template_name = 'inventory/house_confirm_delete.html'
    context_object_name = 'house'
    success_url = reverse_lazy('house_list')


class ProfessorListView(ListView):
    model = Professor
    template_name = 'inventory/professor_list.html'
    context_object_name = 'professors'
    ordering = ['name']


class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'inventory/professor_detail.html'
    context_object_name = 'professor'


class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'inventory/professor_form.html'
    success_url = reverse_lazy('professor_list')


class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'inventory/professor_form.html'

    def get_success_url(self):
        return reverse_lazy('professor_detail', kwargs={'pk': self.object.pk})


class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'inventory/professor_confirm_delete.html'
    context_object_name = 'professor'
    success_url = reverse_lazy('professor_list')
