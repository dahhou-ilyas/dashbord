from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='expenses'),
   path('edit-expense/<int:id>',views.expense_edit,name='expense-edit'),
   path('add-expense', views.add_expences, name="add-expenses"),
   path('delete-expense/<int:id>',views.delet_expense,name='delete-expense')
]
