"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from .views import *



urlpatterns = [
    path('event/', EventView.as_view(), name='Event'),
    path('event/<int:pk>/', EventDetails.as_view(), name='EventDetails'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('payment/<int:pk>/', PaymentDetail.as_view(), name='payment-detail'),
    path('attendance/', AttendanceView.as_view(), name='home'),
    path('attendance/<int:pk>/', AttendanceDetail.as_view(), name='home'),
    path('eventstatus/', EventStatusView.as_view(), name='home'),
    path('eventstatus/<int:pk>/', EventStatusDetail.as_view(), name='home'),
    path('rating/', RatingView.as_view(), name='home'),
    path('rating/<int:pk>/', RatingDetail.as_view(), name='home'),
    path('comment/',CommentView.as_view(),name='CommentView'),
    path('comment/<int:pk>/',CommentDetail.as_view(),name='CommentDetail'),

    ]



