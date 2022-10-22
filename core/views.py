from django.shortcuts import render
from rest_framework.response import Response
from rest_auth.views import APIView
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data)