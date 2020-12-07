from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('employee_profile/', views.profile, name='profile'),
    path('edit_information/', views.Sign, name='edit'),
    path('employee_dashboard/', views.e_dash, name='emp_dash'),
    path('admin_dashboard/', views.a_dash, name='adm_dash'),
    path('leave/', views.leave, name='leave'),
    path('conveyance_expenses/', views.conveyance, name='convey'),
    path('holiday_overtime/', views.holiday, name='hol_ovr'),
    path('regular_overtime/', views.regular, name='reg_ovr'),
    path('pending_applications/', views.pending, name='pending'),
]
