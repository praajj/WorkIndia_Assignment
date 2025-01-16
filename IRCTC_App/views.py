from django.shortcuts import render, HttpResponse

# Create your views here.
# def index(request):
#    return HttpResponse("Home Page")

def SignUpPage(request):
   return render(request,'signup.html')

def LoginPage(request):
   return render(request,'login.html')

def HomePage(request):
   return render(request,'home.html')


