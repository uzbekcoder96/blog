from django import forms
from users.models import CustomUser

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120, required=True, label='Username')
    email = forms.EmailField(max_length=120, required=True, label='Elektron Pochta')
    password = forms.CharField(max_length=100, label='Parol',
                        widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=100, label='Parolni tasdiqlash',
                        widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fileds = ['username', 'email', 'password', 'password_confirmation']
    
        labels = {
                'first_name': 'Ism',
                'last_name': 'Familiya'
            }

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu nomdagi foydalanuvchi allaqochon ro\'yxatdan o\'tgan')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Ushbu email sistemada ro\'yxatdan o\'tkazilgan.')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Parol end kamida 8 ta belgidan iborat bo\'lishi kerak') 
        if password.isnumeric():
            raise forms.ValidationError('Parolda eng kamida bitta harf ishtirok etishi kerak')
        if password.isalpha():
            raise forms.ValidationError('Parolda end kamida bitta son ishtirok etishi kerak')  

        return password                 
    
    def clean_confirm_password(self):
        password = self.data['password']
        confirm_password = self.cleaned_data['password_confirmation']
        if password != confirm_password:
            raise forms.ValidationError('Tasdiqlash paroli notogri')

        return confirm_password