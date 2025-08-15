from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from django.shortcuts import render




def home(request):
    return render(request, 'index.html')

def expenses_page(request):
    return render(request, 'expenses.html')

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer