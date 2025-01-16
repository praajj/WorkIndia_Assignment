from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from .models import User


def SignUpPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})
        
        if User.objects.filter(username=user_name).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
         
        if pass1 != pass2:
         return render(request, 'signup.html', {'error': 'Passwords do not match'})
        print(user_name, email, pass1, pass2)
        
        try:
            hashed_password = make_password(pass1)
            new_user = User(username=user_name, email=email, password=hashed_password)
            new_user.save()
            return redirect('login') 
        except Exception as e:
            return render(request, 'signup.html', {'error': f'Error saving user: {str(e)}'})

    else:
        return render(request, 'signup.html')
     

def LoginPage(request):
    return render(request, 'login.html')

def HomePage(request):
   return render(request,'home.html')

# Logout view
def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('signup')  # Redirects to the home page after logging out

# Book Train view
def book_train(request):
    return render(request, 'book_train.html')


