import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Expense, Budget

# Home UI
def home(request):
    return render(request, 'index.html')

# Add Expense
@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Expense.objects.create(**data)
        return JsonResponse({"message": "Expense added successfully"})
    return JsonResponse({"error": "POST required"}, status=405)

# View Expenses
def view_expenses(request):
    return JsonResponse(list(Expense.objects.values()), safe=False)

# Delete Expense
@csrf_exempt
def delete_expense(request, id):
    Expense.objects.filter(id=id).delete()
    return JsonResponse({"message": "Expense deleted successfully"})

# Set Budget
@csrf_exempt
def set_budget(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Budget.objects.update_or_create(id=1, defaults=data)
        return JsonResponse({"message": "Budget set successfully"})
    return JsonResponse({"error": "POST required"}, status=405)

# Dashboard
def dashboard(request):
    total = sum(e.amount for e in Expense.objects.all())
    budget_obj = Budget.objects.first()
    budget = budget_obj.amount if budget_obj else 0
    return JsonResponse({
        "total_spent": total,
        "budget": budget,
        "remaining": budget - total
    })

# Health Check
def health(request):
    return JsonResponse({"status": "OK"})
