from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Category,Expense
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
# Create your views here.

def search_expenses(request):
    if request.method=="POST":
        
        search_str=json.loads(request.body).get('searchText')
       
        expenses=Expense.objects.filter(amount__istartswith=search_str,owner=request.user) | Expense.objects.filter(date__istartswith=search_str,owner=request.user) | Expense.objects.filter(description__icontains=search_str,owner=request.user) | Expense.objects.filter(category__icontains=search_str,owner=request.user)
    
    data=expenses.values()
    return JsonResponse(list(data),safe=False)

@login_required(login_url="/authentication/login")
@never_cache
def index(request):
    category=Category.objects.all()
    expenses=Expense.objects.filter(owner=request.user)
    paginator=Paginator(expenses,3)
    page_number=request.GET.get("page")
    page_obj=Paginator.get_page(paginator,page_number)
    
    context={
        'expenses':expenses,
        'page_obj':page_obj
    }
    return render(request,'expenses/index.html',context)

@login_required(login_url="/authentication/login")
@never_cache
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



@login_required(login_url="/authentication/login")
@never_cache
def expense_edit(request,id):
    category=Category.objects.all()
    expense=Expense.objects.get(pk=id)
    context={
        'expense':expense,
        'values':expense,
        'categories':category
    }
    
    if request.method=="POST":
        amount=request.POST['amount']
        description=request.POST['description']
        expense_date=request.POST['expense_date']
        categori=request.POST['category']
        if not amount:
            messages.error(request,'Ammount is required')
            return render(request,'expenses/edit-expense.html',context)
        if not description:
            messages.error(request,'description is required')
            return render(request,'expenses/edit-expense.html',context)
        
        expense.owner=request.user
        expense.amount=amount
        expense.date=expense_date
        expense.category=categori
        expense.description=description
        expense.save()
        messages.success(request,'Expense Update succesffuly')
        return redirect('expenses')
    
    return render(request,'expenses/edit-expense.html',context)

def delet_expense(request,id):
    expense=Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request,'Expense Delet succesffuly')
    return redirect('expenses')