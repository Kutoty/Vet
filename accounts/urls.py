from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('register', views.registration_view, name="registration_view"),
    path('vetregister', views.create_vet_account, name="create_vet_account"),
    path('logout',views.login_view,name="logout")
]
    
