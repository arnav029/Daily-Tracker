from django.urls import path, include
from rest_framework import routers
from expenses.views import ExpenseViewSet, home, expenses_page

router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')


urlpatterns = [

    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('expenses/', expenses_page),    
]
