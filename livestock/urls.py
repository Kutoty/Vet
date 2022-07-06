from django.urls import path
from . import views
urlpatterns = [
    path('users/admin', views.admin_home_dashboard, name="admin_home_dashboard"),
    path('users/common', views.farmer_home_view, name="farmer_home_view"),
    path('users/vet', views.vet_home_view, name="vet_home_view"),
    path('users/breed',views.add_breed,name="add_breed"),
    path('animals',views.add_animal,name="add_animal"),
    path('bookvet',views.book_vet,name="book_vet"),
    path('specialization',views.add_specialization,name="add_specialization"),
]
