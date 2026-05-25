
from django.shortcuts import render
from django.http import JsonResponse
from .models import Expense, Budget
from django.views.decorators.csrf import csrf_exempt
import json
 
# Home Page (Frontend UI)
def home(request):
    return render(request, 'index.html')
 
 
# Add Expense
@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
 
            Expense.objects.create(
                category=data.get('category'),
                amount=data.get('amount'),
                date=data.get('date')
            )
 
            return JsonResponse({"message": "Expense added successfully"})
       
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
 
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
 
 
#  View Expenses
def view_expenses(request):
    expenses = list(Expense.objects.values())
    return JsonResponse(expenses, safe=False)
 
 
# Set Budget
@csrf_exempt
def set_budget(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
 
            # Keep only one budget (PoC purpose)
            Budget.objects.all().delete()
 
            Budget.objects.create(
                month=data.get('month'),
                amount=data.get('amount')
            )
 
            return JsonResponse({"message": "Budget set successfully"})
       
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
 
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
 
 
# Dashboard
def dashboard(request):
    expenses = Expense.objects.all()
    total = sum(e.amount for e in expenses)
 
    budget = Budget.objects.first()
    budget_amount = budget.amount if budget else 0
 
    return JsonResponse({
        "total_spent": total,
        "budget": budget_amount,
        "remaining": budget_amount - total
    })
 
 
#  Health API (for Grafana)
def health(request):
    return JsonResponse({"status": "OK"})
 