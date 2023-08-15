from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages
# Create your views here.

def index(request):
    currency_data=[]
    file_path=os.path.join(settings.BASE_DIR,'currencies.json')
    
    with open(file_path,"r") as json_file:
        data=json.load(json_file)
        for k,v in data.items():
            currency_data.append({'name':k,'value':v})
            
        
    use_preferences=None
    existe=UserPreference.objects.filter(user=request.user).exists()
    
    if existe:
       use_preferences= UserPreference.objects.get(user=request.user)
   
    if request.method=='GET':
        return render(request,'preferences/index.html',{'currencies':currency_data})
    else:
        currency=request.POST['currency']
        print(currency)
        if existe:
            use_preferences.currency=currency
            use_preferences.save()
            messages.success(request,'changes saved')
            return render(request,'preferences/index.html',{'currencies':currency_data})
        else:  
            UserPreference.objects.create(user=request.user,currency=currency)
            messages.success(request,'changes saved')
        return render(request,'preferences/index.html',{'currencies':currency_data})