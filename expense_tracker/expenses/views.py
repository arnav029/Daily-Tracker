from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'index.html')

def expenses_page(request):
    return render(request, 'expenses.html')

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]  # ✅ Ensure only logged-in users can access

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)  # ✅ Filter by current user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # ✅ Automatically set user on creation