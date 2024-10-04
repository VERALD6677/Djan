from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('current_time/', views.current_time, name='current_time'),
    path('workdir/', views.workdir, name='workdir'),
]