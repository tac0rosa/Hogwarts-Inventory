from django import forms

from .models import House, Professor, Student, Item


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'founder', 'common_room', 'points']


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name', 'subject', 'office', 'house']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'year', 'house', 'advisor']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'description', 'house', 'owner']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
