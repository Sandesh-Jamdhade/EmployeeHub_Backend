from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee_list),
    path("employees/create/", views.employee_create),
    path("employees/<int:id>/", views.employee_detail),
    path("employees/update/<int:id>/", views.employee_update),
    path("employees/delete/<int:id>/", views.employee_delete),
    path("login/", views.login_api),
    path("register/", views.register_api),
    path("is-admin/", views.is_admin),
]
