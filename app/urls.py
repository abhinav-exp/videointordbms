from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fooset/', views.fooview),
    path('fooget/<int:id>/', views.fooret),
]