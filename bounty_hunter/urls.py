from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bounty.as_view(), name='bounty'),
    path('bounty/<int:pk>/', views.Task.as_view(), name='one-bounty')
]