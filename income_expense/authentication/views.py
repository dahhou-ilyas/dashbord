from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from validate_email import validate_email
from django.contrib import messages

# Create your views here.
class UsernameValidation(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']
        
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username only with alphanumerique char'},status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username is existe,chose another one'},status=409)
        
        return JsonResponse({'username-valid':True})
    
    
class EmailValidation(View):
    def post(self,request):
        data=json.loads(request.body)
        email=data['email']
        
        if not validate_email(email):
            return JsonResponse({'email_error':'email is invalide'},status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'email is exist try another one'},status=409)
        
        return JsonResponse({'email-valid':True})
    
    
class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/registre.html')
    
    def post(self,request):
        
        messages.success(request,'Success whatsapp')
        messages.warning(request,'Success whatsapp')
        messages.info(request,'Success whatsapp')
        messages.error(request,'Success whatsapp')
    
        return render(request,'authentication/registre.html')