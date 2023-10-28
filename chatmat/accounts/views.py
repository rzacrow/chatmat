from django.shortcuts import render
from django.views.generic import View, FormView, CreateView, TemplateView
from .forms import LoginForm

class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        
        return render(request, 'login.html', context)
    
class Signup(View):
    pass
    
class Logout(View):
    pass

class ForgetPassword(View):
    pass

class ResetPassword(View):
    pass

class Confirmation(View):
    pass