from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('houses/', views.HouseListView.as_view(), name='house_list'),
    path('houses/<int:pk>/', views.HouseDetailView.as_view(), name='house_detail'),
]
