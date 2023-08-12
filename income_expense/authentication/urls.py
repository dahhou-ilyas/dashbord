from .views import RegistrationView
from django.urls import path

urlpatterns = [
    path('registre',RegistrationView.as_view(),name='registre')
]
