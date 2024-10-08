from django.urls import path, re_path
from app import views

urlpatterns = [
    re_path(r'^main/.*$', views.main, name="home"),  # Главная страница приложения
    re_path(r'^news/.*$', views.news, name="news"),  
    re_path(r'^management/.*$', views.management, name="management"),  
    re_path(r'^about/.*$', views.about, name="about"),  
    re_path(r'^contacts/.*$', views.contacts, name="contacts"), 
    path('branches/<str:city_name>/', views.get_branch),  
    re_path(r'^branches/.*$', views.branches, name="branches"), 

    re_path(r"^.*$", views.main, name="home")
]