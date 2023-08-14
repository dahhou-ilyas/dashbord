from .views import RegistrationView,UsernameValidation,EmailValidation,LoginView,LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('registre',RegistrationView.as_view(),name='registre'),
    path('login',LoginView.as_view(),name='login'),
    path('valide-username',csrf_exempt(UsernameValidation.as_view()),name='validation username'),
    path('valide-email',csrf_exempt(EmailValidation.as_view()),name='validation email'),
    path('logout',LogoutView.as_view(),name="logout")
]
