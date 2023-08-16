from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Category,Expense
from django.contrib import messages
# Create your views here.

@login_required(login_url="/authentication/login")
@never_cache
def index(request):
    
    category=Category.objects.all()
    expenses=Expense.objects.filter(owner=request.user)
    context={
        'expenses':expenses
    }
    return render(request,'expenses/index.html',context)

def add_expences(request):
    category=Category.objects.all()
    context={
        'categories':category,
        'values':request.POST
    }


    if request.method=='POST':
        amount=request.POST['amount']
        description=request.POST['description']
        expense_date=request.POST['expense_date']
        categori=request.POST['category']
        if not amount:
            messages.error(request,'Ammount is required')
            return render(request,'expenses/add_expense.html',context)
        if not description:
            messages.error(request,'description is required')
            return render(request,'expenses/add_expense.html',context)
        Expense.objects.create(owner=request.user,amount=amount,date=expense_date,
                               category=categori,description=description)
        messages.success(request,'Expense saved succesffuly')
        return redirect('expenses')
    return render(request,'expenses/add_expense.html',context)
        
    