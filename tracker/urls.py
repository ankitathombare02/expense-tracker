# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home), 
#     path('add-expense/', views.add_expense),
#     path('view-expenses/', views.view_expenses),
#     path('set-budget/', views.set_budget),
#     path('dashboard/', views.dashboard),
#     path('health/', views.health),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),                         # ✅ frontend page

    path('add-expense/', views.add_expense),      # ✅ add expense
    path('view-expenses/', views.view_expenses),  # ✅ view expenses

    path('delete-expense/<int:id>/', views.delete_expense),  # ✅ delete expense

    path('set-budget/', views.set_budget),        # ✅ set budget
    path('dashboard/', views.dashboard),          # ✅ dashboard

    path('health/', views.health),                # ✅ health API
            # ✅ reset all data
]