from django.urls import reverse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from .utils import generate_token
from .models import CustomUser
from users.forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
USER = get_user_model()
# from django.contrib.auth.forms import UserCreationForm

#for password reset 
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

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
                    subject="BlogUz activatsiya",
                    message="Iltimos accauntingizni activ qilish uchun ushbu " +
                            f"link http://127.0.0.1:8000/users/{user.id}/verify/{fields['token_for_activation']}" +
                            " linkka bosing")
                           
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
   
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def verify_email_view(request, user_id, token):
    user = USER.objects.filter(id=user_id).first()
    if user and user.token_for_activation == token:
        user.is_active = True
        user.token_for_activation = ''
        user.save()
        return render(request, "login.html", {})
    
    return render(request, "success.html", {})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    # subject_template_name = 'password_reset_subject.txt'
    success_message = "Passwordni o'zgartirish uchun kiritilgan emailga xxabar jo'natdik iltimos tekshirib ko'ring " \
                      "Agar ro'yxatdan o'tgan to'g'ri email kiritgan bo'lsangiz emailingizga xabar yuborildi" \
                      "Iltimos ro'yxatdan o'tgan emailingizni kiritganingizga amin bo'ling Agar bormagan bo'lsa spamni tekshirib ko'ring"
    success_url = reverse_lazy('users:login')


