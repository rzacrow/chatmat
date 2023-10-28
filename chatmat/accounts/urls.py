from django.urls import path
from .views import Login, Signup, Logout, ForgetPassword, ResetPassword, Confirmation

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('forgetpassword/', ForgetPassword.as_view(), name='forgetpassword'),
    path('resetpassword/', ResetPassword.as_view(), name='resetpassword'),
    path('confirmation/', Confirmation.as_view(), name='confirmation'),
]
