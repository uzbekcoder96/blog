from django.urls import reverse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from .utils import generate_token
from users.forms import RegisterForm, LoginForm
USER = get_user_model()
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_view(request):

    form = RegisterForm(request.POST or None) # RegisterForm()

    if request.method == 'POST':
        if form.is_valid():
            fields = form.cleaned_data
            del fields['password_confirmation']
            fields['token_for_activation'] = generate_token(45)
            user = USER.objects.create_user(**fields)
            try:
                email_sent = user.email_user(
                    subject="Verify your email on Havola.uz",
                    message="Please verify your email using this" +
                            f"link http://127.0.0.1:8000/users/{user.id}/verify/{fields['token_for_activation']}" +
                            " to activate your account")
                           
            except Exception as e:
                print(e)
                email_sent = False

            return  redirect(reverse('users:login'), data={'email-sent':bool(email_sent)})
            

        
    return render(request, 'register.html', {'form': form})
   

def login_view(request):

   
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = USER.objects.get(username=username)
            login(request, user)
            return redirect(reverse('blog:home')) # /users/check-user

    return render(request, "login.html", {'form': form})

def logout_view(request):
    print(request.user) # AnonymousUser, <User: Admin>
    if request.user.is_authenticated:
        print('login qilgan')
    else:
        print('nomalum foydalanuvchi')
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def verify_email_view(request, user_id, token):
    user = USER.objects.filter(id=user_id).first()
    if user and user.token_for_activation == token:
        user.is_active = True
        user.token_for_activation = ''
        user.save()
        return render(request, "login.html", {})
    
    return render(request, "verify-fail.html", {})
    