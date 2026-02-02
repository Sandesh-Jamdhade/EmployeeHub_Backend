from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/create/', views.employee_create),
    path('employees/<int:id>/', views.employee_detail),
    path('employees/<int:id>/update/', views.employee_update),
    path('employees/<int:id>/delete/', views.employee_delete),
]
