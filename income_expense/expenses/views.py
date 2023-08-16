from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Category,Expense
from django.contrib import messages
# Create your views here.

@login_required(login_url="/authentication/login")
@never_cache
def index(request):
    category=Category.objects.all()
    return render(request,'expenses/index.html')

def add_expences(request):
    category=Category.objects.all()
    context={
        'categories':category,
        'values':request.POST
    }
    print(request.POST)

    if request.method=='POST':
        amount=request.POST['amount']
        description=request.POST['description']
        if not amount:
            messages.error(request,'Ammount is required')
            return render(request,'expenses/add_expense.html',context)
        if not description:
            messages.error(request,'description is required')
            return render(request,'expenses/add_expense.html',context)
    return render(request,'expenses/add_expense.html',context)
        
    