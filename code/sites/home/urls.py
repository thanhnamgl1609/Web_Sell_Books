from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('search',views.search),
    path('<int:id>/',views.by_category, name = 'home')
]
