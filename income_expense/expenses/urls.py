from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='expenses'),
   path('add-expense', views.add_expences, name="add-expenses"),
]
