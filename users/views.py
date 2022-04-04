from django.shortcuts import render

from django.contrib.auth import get_user_model
USER = get_user_model()
# from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
# Create your views here.

def register_view(request):

    form = RegisterForm(request.POST or None) # RegisterForm()

    if request.method == 'POST':
        if form.is_valid():
            fields = form.cleaned_data
            del fields['password_confirmation']
            user = USER.objects.create_user(**fields)
            return render(request, 'finish.html', {})

    return render(request, 'register.html', {'form': form})

   

def login_view(request):

    context = {}

    return render(request, 'login.html', context)

def logout_view(request):

    context = {}

    return render(request, 'login.html', context)