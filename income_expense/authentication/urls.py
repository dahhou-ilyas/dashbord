from .views import RegistrationView,UsernameValidation
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('registre',RegistrationView.as_view(),name='registre'),
    path('valide-username',csrf_exempt(UsernameValidation.as_view()),name='validation username')
]
