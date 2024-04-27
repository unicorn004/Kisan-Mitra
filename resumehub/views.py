from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage/index.html')

@login_required(login_url = 'accounts:login')
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)

def login_page(request):
    form = AuthenticationForm()
    return render(request, 'user_login/login.html', {'form': form})

def profile_view(request):
    return render(request, 'profile/profile.html')

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')

def create_profile(request):
    return render(request, 'profiles/create_profile.html')

def estore(request):
    return render(request, 'estore.html')

<<<<<<< HEAD
def organicservice(request):
    return render(request, 'organicservice.html')
=======
def rice(request):
    return render(request, 'rice.html')
>>>>>>> a6dc3c4ac1c6baf2ddad441d4a5e7a44a9072df7
