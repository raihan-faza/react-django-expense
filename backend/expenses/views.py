from rest_framework import permissions

from .base import BaseViewSet
from .models import Expense, Wallet
from .serializers import ExpenseSerializer, WalletSerializer


class ExpenseViewSet(BaseViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Expense.objects.all()


class WalletViewSet(BaseViewSet):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Wallet.objects.all()
