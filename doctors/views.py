from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm
from .models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import AuthenticationForm


import qrcode
import qrcode.image.svg
from io import BytesIO
from django.shortcuts import render
from .models import Doctor


def doctor_profile(request):
    doctor = Doctor.objects.get(user=request.user)
    qr_text = f"Doctor: {doctor.first_name} {doctor.last_name}, Email: {doctor.email}"

    qr_code = {}

    factory = qrcode.image.svg.SvgImage
    buffer = BytesIO()
    img = qrcode.make(qr_text, image_factory=factory, box_size=20)
    img.save(buffer)
    buffer.seek(0)
    qr_code["svg"] = buffer.getvalue().decode()
    
    return render(request, 'doctors/doctor_profile.html', {'doctor': doctor, 'qr_code': qr_code})


def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            # Создание пользователя
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            # Создание объекта Doctor и привязка к пользователю
            doctor = Doctor.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                organization=form.cleaned_data['organization']
                # Другие поля
            )
            # Дополнительные действия после успешной регистрации врача
            return redirect('login_form')  # Перенаправление на личный кабинет после успешной регистрации
    else:
        form = DoctorRegistrationForm()
    
    return render(request, 'doctors/register_doctor.html', {'form': form})


def oferta_page(request):
    # Ваша логика представления для страницы с PDF
    return redirect('https://pets.smartbreeding.ru/oferta')


def privacy_page(request):
    return redirect('https://pets.smartbreeding.ru/privacy')


def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Перенаправление пользователя на нужную страницу после входа
                return redirect('doctor_profile')  # Или на любую другую страницу
    else:
        form = AuthenticationForm()
    return render(request, 'doctors/login_form.html', {'form': form})

def client_registration(request, qr_code):
    # Логика обработки регистрации клиента по QR-коду
    pass

def generate_qr_code(request):
    # Логика генерации QR-кода для врача
    pass
