from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json


# Create your views here.
class UsernameValidation(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']
        
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username only with alphanumerique char'},status=400)
        
        return JsonResponse({'username-valid':username})
    
class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/registre.html')