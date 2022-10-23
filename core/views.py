from unicodedata import category
from django.shortcuts import render
from rest_framework.response import Response
from rest_auth.views import APIView
from .models import Category, PiggyBank, Transaction, UserSavings
from .serializers import CategorySerializer, PiggyBankSerializer
# Create your views here.
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny
from typing import List, Any


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data)

class TransactionView(APIView):
    authentication_classes: List = []
    permission_classes: List[Any] = [AllowAny]

    
    def post(self, request):
        try:
            tr = Transaction(
                amount=int(request.POST.get("amount")),
                category=Category.objects.get(pk=int(request.POST.get("category"))),
                user=int(request.POST.get("user"))
            )
            tr.save()
            try:
                usgs = UserSavings.objects.get(user=tr.user)
                pgbk = PiggyBank.objects.filter(user=tr.user, category=tr.category)
                if pgbk:
                    pgbk = pgbk[0]
                    pgbk.current_amount += pgbk.acummulating_rate * tr.amount
                    pgbk.save()
            except:pass
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            return Response(e)


class PiggyBankView(APIView):
    authentication_classes: List = []
    permission_classes: List[Any] = [AllowAny]

    def get(self, request):
        pbs = PiggyBank.objects.filter(user=int(self.request.query_params.get('user')))
        data = PiggyBankSerializer(pbs, many=True).data
        data = {
            "piggy_banks": data,
            "user_bank": UserSavings.objects.get(user=int(self.request.query_params.get('user'))).amount
        }
        return Response(data)

    def post(self, request):
        CATEGORIES = {
            'ENTERTAINMENT': 6,
            'TRANSPORTATION': 5,
            'CLOTHES': 4,
            'GROCERIES': 2,
            'FOOD': 1,
        }
        # print(request.POST)
        # print("asdf")
        print(request.data)
        # print(request.data["limit"])
        try:
            pb = PiggyBank(
                limit=int(request.data['budgetLimit']),
                category=Category.objects.get(pk=CATEGORIES[request.data['type']]),
                acummulating_rate=float(request.data["rate"]),
                user=1,
                name=request.data['name'],
            )
            pb.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e)

