from rest_framework import serializers
from . models import Category, PiggyBank

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name',)


class PiggyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiggyBank
        fields = ('category', 'limit', 'acummulating_rate', 'current_amount', 'total_amout', 'name')