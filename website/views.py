from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
#def home(request):
#    return render(request, 'home.html')


def home(request):
#    if request.user.is_authenticated:
#        return redirect('dashboard')
#    return render(request, 'home_public.html')
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def tables_view(request):
    return render(request, 'tables.html')

def charts_view(request):
    return render(request, 'charts.html')

def buttons_view(request):
    return render(request, 'buttons.html')

def cards_view(request):
    return render(request, 'cards.html')        

def blank_view(request):
    return render(request, 'blank.html')            

def forgot_password_view(request):
    return render(request, 'forgot-password.html')

def utilities_animation_view(request):
    return render(request, 'utilities-animation.html')

def utilities_border_view(request):
    return render(request, 'utilities-border.html')

def utilities_color_view(request):
    return render(request, 'utilities-color.html')    

def utilities_other_view(request):
    return render(request, 'utilities-other.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')    
