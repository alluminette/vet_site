from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.doctor_profile, name='doctor_profile'),
    path('register/<str:qr_code>/', views.client_registration, name='client_registration'),
    path('generate_qr/', views.generate_qr_code, name='generate_qr_code'),
    path('register/', views.register_doctor, name='register_doctor'),
    path('login/', views.login_form, name='login_form')
]
