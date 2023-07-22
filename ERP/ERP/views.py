from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import user


def register(request):
    if request.method == 'POST':
        # fn = UsersForm(request.POST)
        # if fn.is_valid():
            name = request.POST['name']
            address = request.POST['address']
            email = request.POST['email']
            phone = request.POST['phone']
            registrationNo = request.POST['registrationNo']
            verified = request.POST['verified']
            created = request.POST['created']
            status = request.POST['status']

            # Save data to the database
            
            add_company = user(
            name=name,
            address=address,
            email=email,
            phone=phone,
            registrationNo=registrationNo,
            verified=verified,
            created=created,
            status=status)
            print("Name:", name)
            print("Address:", address)
            print("Email:", email)
            print("Phone:", phone)
            print("Registration Number:", registrationNo)
            print("Verified:", verified)
            print("Created:", created)
            print("Status:", status)
    
            add_company.save()
           
    return render(request, 'register.html')
