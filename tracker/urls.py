
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),                        

    path('add-expense/', views.add_expense),     
    path('view-expenses/', views.view_expenses),  
    path('set-budget/', views.set_budget),       
    path('dashboard/', views.dashboard),          

    path('health/', views.health),               
            
]