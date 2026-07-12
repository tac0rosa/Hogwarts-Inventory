from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('houses/', views.HouseListView.as_view(), name='house_list'),
    path('houses/new/', views.HouseCreateView.as_view(), name='house_create'),
    path('houses/<int:pk>/', views.HouseDetailView.as_view(), name='house_detail'),
    path('houses/<int:pk>/edit/', views.HouseUpdateView.as_view(), name='house_update'),
    path('houses/<int:pk>/delete/', views.HouseDeleteView.as_view(), name='house_delete'),
    path('professors/', views.ProfessorListView.as_view(), name='professor_list'),
    path('professors/new/', views.ProfessorCreateView.as_view(), name='professor_create'),
    path('professors/<int:pk>/', views.ProfessorDetailView.as_view(), name='professor_detail'),
    path('professors/<int:pk>/edit/', views.ProfessorUpdateView.as_view(), name='professor_update'),
    path('professors/<int:pk>/delete/', views.ProfessorDeleteView.as_view(), name='professor_delete'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/new/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
