from datetime import time
import threading
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Profile, Patient, Center
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CenterForm


# Create your views here.

def index(request):
    return render(request, 'narcotrack.html')

def search_by_cnic(request):
    if request.method == 'GET':
        cnic = request.GET.get('cnic')
        results = []
        if cnic:
            results = Patient.objects.filter(cnic__icontains=cnic)
        return render(request, 'cnic.html', {'cnic': cnic, 'results': results})
    return render(request, 'cnic.html')



def quiz(request):
    return render(request, 'quiz.html')
 
def create_center(request):
    if request.method == 'POST':
        form = CenterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/centers')  # Redirect to a success page after form submission
    else:
        form = CenterForm()
    return render(request, 'create_center.html', {'form':form})

def patient_data(request):
    if request.method == 'POST':
        if 'patient_id' in request.POST:
            patient_id = request.POST['patient_id']
            patient = Patient.objects.get(id=patient_id)
            
            patient.name = request.POST['name']
            patient.father_name = request.POST['fname']
            patient.gender = request.POST['gender']
            patient.age = request.POST['age']
            patient.cnic = request.POST['cnic']
            patient.phone_number = request.POST['number']
            patient.drug_addiction = request.POST['drug-info']
            patient.fees = request.POST['fees']
            patient.plan = request.POST['plan']
            
            patient.save()
        else:
            name = request.POST['name']
            fname = request.POST['fname']
            gender = request.POST['gender']
            age = request.POST['age']
            cnic = request.POST['cnic']
            number = request.POST['number']
            drug_addiction = request.POST['drug-info']
            fees = request.POST['fees']
            plan = request.POST['plan']
            
            patient = Patient(name=name, father_name=fname, gender=gender, age=age, cnic=cnic, phone_number=number, drug_addiction=drug_addiction, plan=plan, fees=fees)
            patient.save()

        
        return redirect('/patient_data')
    else:
        # Handle GET request
        patients = Patient.objects.all()
        return render(request, 'patient_data.html', {'patients': patients})

def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect ('/patient_data')


def show_profile(request):
    profiles= Profile.objects.filter(user=request.user)
    return render(request,'show_profile.html', {'profiles':profiles})

def centers(request):
    centers = Center.objects.all()
    return render(request,'centers.html', {'centers':centers})

def center_detail(request, id):
    center = Center.objects.select_related('Profile').get(id=id)
    return render(request, 'center_detail.html', {'center': center})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['log-uname']
        password = request.POST['log-pass']
        loginn = authenticate(username=username, password=password)
        if loginn is not None:
            login(request, loginn)
            messages.success(request, 'SuccessFully Login')
            return redirect('/')
        else:
            messages.warning(request, 'Check Your Password or Username')
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('/')
def register(request):
    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'This email address is already in use')
                return redirect('register')
            register = User.objects.create_user(
            uname, email, pass1)
            register.first_name = fname
            register.last_name = lname
            register.save()
            messages.success(request, 'Register Successfully')
            return redirect('login')
        elif pass1 != pass2:
            messages.warning(request, 'Sorry, your password was not same. Please double-check your password')
        
    return render(request, 'register.html')


@login_required(login_url='/login')
def create_profile(request):
    if request.method == 'POST':
        user = request.user
        username = request.user.username
        user = User.objects.get(username=username)
        user.first_name = request.POST.get('pfname')
        user.last_name = request.POST.get('plname')
        user.email = request.POST.get('pemail')
        user.save()
        
        phone_number = request.POST.get('pnumber')
        address = request.POST.get('address')
        cnic = request.POST.get('cnic')
        postal_code = request.POST.get('postalcode')
        education = request.POST.get('education')
        gender = request.POST.get('gender')
        designation = request.POST.get('designation')
        country = request.POST.get('country')
        province = request.POST.get('province')
        experience = request.POST.get("experience")
        additional_details = request.POST.get("additional_information") 

        profile = Profile.objects.filter(user=user).first()
        if profile is None:
            profile = Profile(user=user)

        profile.phone_number = phone_number or profile.phone_number
        profile.postal_code = postal_code or profile.postal_code
        profile.province = province or profile.province
        profile.education = education or profile.education
        profile.address = address or profile.address
        profile.country = country or profile.country
        profile.gender = gender or profile.gender
        profile.designation = designation or profile.designation
        profile.experience = experience or profile.experience
        profile.additional_details = additional_details or profile.additional_details 
        
        profile.cnic = cnic or profile.cnic
        profile.save()
        
        return redirect('/show_profile')
    else:
        profiles= Profile.objects.filter(user=request.user)
        return render(request, 'Profile.html', {'profiles':profiles})




