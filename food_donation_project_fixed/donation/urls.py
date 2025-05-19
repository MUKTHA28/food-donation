from django.urls import path
from . import views

urlpatterns = [
    path('report_food/', views.report_food, name='report_food'),
    path('food_detail/<int:report_id>/', views.food_detail, name='food_detail'),
    path('login/', views.user_login, name='login'),
]
