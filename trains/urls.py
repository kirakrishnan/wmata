from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:locationCode_db>/', views.trainDetails, name = 'trainDetails')
]