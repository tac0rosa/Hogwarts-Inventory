from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('houses/', views.HouseListView.as_view(), name='house_list'),
    path('houses/new/', views.HouseCreateView.as_view(), name='house_create'),
    path('houses/<int:pk>/', views.HouseDetailView.as_view(), name='house_detail'),
    path('houses/<int:pk>/edit/', views.HouseUpdateView.as_view(), name='house_update'),
    path('houses/<int:pk>/delete/', views.HouseDeleteView.as_view(), name='house_delete'),
]
