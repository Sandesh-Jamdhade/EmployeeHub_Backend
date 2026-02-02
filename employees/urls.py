from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/create/', views.employee_create),
]
