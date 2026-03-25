from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('post/', views.post_property, name='post_property'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('delete/<int:pk>/', views.delete_property, name='delete_property'),
    path('my-messages/', views.my_messages, name='my_messages'),
    path('edit/<int:pk>/', views.edit_property, name='edit_property'),
]