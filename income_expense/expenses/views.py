from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@login_required(login_url="/authentication/login")
@never_cache
def index(request):
    return render(request,'expenses/index.html')
