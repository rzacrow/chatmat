from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, label=None, help_text='ایمیل خود را وارد کنید...', required=True)
    password = forms.PasswordInput()
