from django.shortcuts import render


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
