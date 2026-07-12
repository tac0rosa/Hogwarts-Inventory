from django import forms

from .models import House, Professor


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'founder', 'common_room', 'points']


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name', 'subject', 'office', 'house']
