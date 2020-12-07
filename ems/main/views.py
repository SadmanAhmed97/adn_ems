from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('emp_dash')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, "main/login.html")


def logoutUser(request):
    logout(request)
    return redirect('login')


def Sign(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pass')
        department = request.POST.get('dept')
        designation = request.POST.get('des')
        adn_id = request.POST.get('ID')
        email = request.POST.get('mail')
        alt_email = request.POST.get('amail')
        phone = request.POST.get('phone')
        phone_2 = request.POST.get('phone2')
        date_ob = request.POST.get('dob')
        joining = request.POST.get('join')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        blood_g = request.POST.get('blood')

        u = CustomUser(full_name=name, password=password, department=department, designation=designation, adn_id=adn_id,
                       email=email, alternate_email=alt_email, phone=phone, alternate_phone=phone_2, gender=gender,
                       dob=date_ob, join=joining, address=address, blood_group=blood_g)

        u.set_password(password)
        u.save()
        return render(request, "main/employee_dashboard.html")
    else:
        return render(request, "homepage/signup.html")


def profile(request):
    return render(request, "main/employee_profile.html")


def e_dash(request):
    return render(request, "main/employee_dashboard.html")


def a_dash(request):
    return render(request, "main/admin_dashboard.html")


def leave(request):
    return render(request, "main/leave.html")


def conveyance(request):
    return render(request, "main/conveyance.html")


def holiday(request):
    return render(request, "main/hol_overtime.html")


def regular(request):
    return render(request, "main/reg_overtime.html")


def pending(request):
    return render(request, "main/pending.html")
