from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.models import auth
#our useromdel
from django.contrib.auth import get_user_model
# Create your views here.

User= get_user_model()

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        
        # Check if the username exists in the database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # Log the user in without requiring a password
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        # password1 = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        desc = request.POST.get('desc')
        degree = request.POST.get('degree')
        job_role = request.POST.get('job_role')
        # print('DeBUG')

        # if password1 == password2:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('register')
        else:
            user = User(
                username = username,
                email = email,
                image1 = image1,
                image2 = image2,
                desc = desc,
                degree = degree,
                job_role = job_role
            )
            # user.set_password(password1)  # Set password
            user.save()
            print('User Created')
            return redirect('login')
        # render(request, 'register.html')
        # else:
        #     messages.info(request, 'Passwords do not match')
        #     return redirect('register')
    else:
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')